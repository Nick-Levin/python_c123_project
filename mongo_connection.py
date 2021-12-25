from pymongo import MongoClient


def get_events_collection():
    return MongoClient('localhost:27017').test.events
