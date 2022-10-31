from tkinter import messagebox
import pymongo
from bson import ObjectId

connection = pymongo.MongoClient('localhost', 27017)

database = connection['EwasteRecords']
collection = database['myEwasteCollections']
print("Database Connected")


def insert_data(data):
    document = collection.insert_one(data)
    return document.inserted_id


def update_or_create(document_id, data):
    document = collection.update_one(
        {'_id': ObjectId(document_id)}, {"$set": data}, upsert=True)

    return document.acknowledged


def remove_data(document_id):
    document = collection.delete_one({'_id': ObjectId(document_id)})
    return document.acknowledged


def get_single_data(document_id):
    data = collection.find_one({'_id': ObjectId(document_id)})

    return data


def get_multiple_data():
    data = collection.find()
    return list(data)


def update_existing(document_id, data):
    document = collection.update_one(
        {'id': ObjectId(document_id)}, {"$set": data})

    return document.acknowlegde


# 6359e0084774fd6fc5cb09d4
# 6359e14d8cd5ffbd284f0e34
