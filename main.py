from fastapi import FastAPI
from models import Item,UpdateSchema, Delete
from createDB import init_connection, init_db, mongo_import, is_db_created
import json
from bson.json_util import dumps

csv_path = '/home/shahroz/Documents/assignment/Greendeck SE Assignment Task 1.csv'

# Initialising the connection with MongoDB
client = init_connection()
db, coll = init_db(client)

# Inserting data into mongoDB from csv
is_db_created = True #set this to false to insert data into MongoDB

if not is_db_created:
    mongo_import(csv_path,db.name,coll.name,client)
    is_db_created = True

# Creating the FastAPI instance
app = FastAPI()

@app.post('/add-data')
async def add_data(item:Item) -> dict:
    """[Post method to insert data into mongoDB]

    Args:
        item (Item): [Model of the required request body]

    Returns:
        dict: [Result of the query]
    """
    try:
        # Insert into DB
        ret = coll.insert_one(item.dict())
        res = {
            'status' : 201,
            'message': 'Successfully added',
            'data' : item.dict()
        }
    except Exception as e:
        # Return error if any
        res = {
            'status' : '500',
            'error' : 'true',
            'message' : str(e)
        }
    return res

@app.get('/get-data-by-name')
async def get_data(name:str) -> dict:
    """[Get method to get document by passing the name.]

    Args:
        name (str): [name of the required document]

    Returns:
        dict: [Result of the query]
    """
    try:
        # Mongo query to find the data
        data = json.loads(dumps(coll.find({"name":name})))
        print(data)
        # Check if data is not found.j
        if len(data) == 0:
            response = {
                'status' : 200,
                'message' : 'No entry found',
            }
        else:
            response = {
                'status' : 200,
                'message' : 'Successfully fetched',
                'data' : data
            }
    except Exception as e:
        # Return error if any.
        response = {
            'error' : 'True',
            'message' : e
        }
    return response


@app.put('/update-data')
async def update_data(data:UpdateSchema) -> dict:
    """[
        Put method to update existing record in the DB.
        This function will update only one document.
    ]
    Args:
        data (UpdateSchema): [Model for querying DB and updated values]

    Returns:
        dict: [Result of the query]
    """
    data = data.dict()
    temp = {}
    # Creating a dict of values  to be updated
    for i in data:
        if i!='key' and i!='value' and data[i] is not None:
            temp[i] = data[i]
    
    # Creating a dict of query that will find the specific record
    query = {}
    if data["value"].isnumeric():
        query[data["key"]] = int(data["value"])
    else:
        query[data["key"]] = data["value"]
    new_values = {
        "$set" : temp
    }
    try:
        # Update the record
        # To update all of the matching results, change *update_one* method to *update_many*
        ret = coll.update_one(query,new_values)

        # Check if the result is updated
        if ret.raw_result['updatedExisting'] == True:
            res = {
                'status' : 200,
                'message' : 'Successfully Updated',
                'updated' : ret.raw_result
            }
        else:
            res = {
                'status' : 200,
                'message' : 'Document not found',
                'result' : ret.raw_result
            }
    except Exception as e:
        # Return error if any
        res = {
                'error' : 'true',
                'message' : str(e)
            }
    return res


@app.delete('/delete-data')
async def delete_data(query:Delete) -> dict:
    """[Delete method to remove the document of the query passed]

    Args:
        query (Delete): [Function will remove the document based on the query]

    Returns:
        dict: [Result of the query]
    """
    try:
        # If the record exists, it will be deleted
        # Only one document will be removed, to remove all change *delete_one* => *delete_many*
        coll.delete_one(query.dict())
        res = {
            'status' : 200,
            'message' : 'Successfully removed',
            'data' : query.dict()
        }
    except Exception as e:
        # Return error if any
        res = {
            'error' : 'true',
            'message' : str(e)
        }
    return res