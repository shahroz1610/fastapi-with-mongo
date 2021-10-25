import pandas as pd
from pymongo import MongoClient
import json
from dotenv import load_dotenv
import os

load_dotenv()

def init_connection()->MongoClient:
    """[Function to connect service to local MongoDB]

    Returns:
        MongoClient: [Instance of pymongo]
    """
    host = os.getenv('host')
    port = os.getenv('port')
    username = os.getenv('username')
    password = os.getenv('password')
    client = MongoClient(host,port,username=username,password=password)
    return client

def init_db(client,db_name="greendeck",collection_name="customer"):
    """[Function to create collecion and database]

    Returns:
        db -> Instance of created database
        coll -> Instance of created collection
    """
    db = client[db_name]
    db_collection = db[collection_name]
    return db,db_collection

def mongo_import(csv:str,db_name:str,collection_name:str,client:MongoClient):
    """[Function to insert data from CSV to MongoDB]
    """
    db = client[db_name]
    db_collection = db[collection_name]
    data = pd.read_csv(csv,encoding = "ISO-8859-1")
    payload = json.loads(data.to_json(orient='records'))
    # db_collection.remove()
    db_collection.insert(payload)
    return True