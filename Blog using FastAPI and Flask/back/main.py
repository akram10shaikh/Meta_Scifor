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



def document_to_item(data) -> Item:
    return Item(
        id=str(data['_id']),
        title=data['title'],
        description=data['description']
    )

@app.get("/items", response_model=List[Item])
async def get_items():
    items = []
    for doc in collection.find():
        items.append(document_to_item(doc))
    return items