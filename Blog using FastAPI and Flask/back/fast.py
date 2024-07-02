from fastapi import FastAPI
import pymongo
import json
from bson.objectid import ObjectId
from pydantic import BaseModel
from typing import List


app = FastAPI()

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['akram']
collection = db['testing']

data = collection.find({},{'title':1,'description':1})

class Item(BaseModel):
    id: str
    title: str
    description: str



def document_to_item(document) -> Item:
    return Item(
        id=str(document['_id']),
        name=document['name'],
        value=document['value']
    )
