from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Connection to mongodb
def connect():
    client = MongoClient(
        "mongodb+srv://ivmv2007:EJvjkvc7pIaSWO5b@mimongo.uvxb1qp.mongodb.net/?retryWrites=true&w=majority",
        server_api=ServerApi('1')
    )

    db = client.hw10
    return db