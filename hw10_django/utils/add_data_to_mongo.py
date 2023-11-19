#This script adds to the quotes author _id

import json
from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Connection to mongodb
client = MongoClient(
    "mongodb+srv://ivmv2007:EJvjkvc7pIaSWO5b@mimongo.uvxb1qp.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi('1')
)

db = client.hw10

# Add authors.json to MongoDB
with open('authors.json', 'r', encoding='utf-8') as fd:
    authors = json.load(fd) 

for author in authors:
    db.authors.insert_one({
        'fullname': author['fullname'],
        'born_date': author['born_date'],
        'born_location': author['born_location'],
        'description': author['description']      
    })

# Add quotes to Mongodb
with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd) 
# Changing the quotes;
for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })

# To run script go to the script location: D:\VSCode_projects\Python-web-hw10\hw10_django\utils