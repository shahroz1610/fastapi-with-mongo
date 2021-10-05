import pandas as pd
from pymongo import MongoClient
import json
# import os

# MONGO_USER = os.environ['MONGO_ROOT_USER']
# MONGO_PASSWORD = os.environ['MONGO_ROOT_PASSWORD']
# print(MONGO_USER,MONGO_PASSWORD)

# Indicates whether the data from CSV is inserted into MongoDB
is_db_created = False

# Function to connect service to local MongoDB
def init_connection():
    client = MongoClient(username='admin',password='admin@123')
    return client

# Function to create collecion and database
def init_db(client,db_name="greendeck",coll_name="customer"):
    # client = MongoClient(url,port)
    db = client[db_name]
    coll = db[coll_name]
    return db,coll

# Function to insert data from CSV to MongoDB
def mongo_import(csv:str,db_name:str,coll_name:str,client:MongoClient):
    db = client[db_name]
    coll = db[coll_name]
    data = pd.read_csv(csv,encoding = "ISO-8859-1")
    payload = json.loads(data.to_json(orient='records'))
    coll.remove()
    coll.insert(payload)
    return True