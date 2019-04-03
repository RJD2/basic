from pymongo import MongoClient
import config


connection = None


def get_connection(pullSize=1024):
    global connection
    if not connection:
        connection = MongoClient(
            config.MONGODB_SETTINGS.get('HOST'),
            connect=False,
            maxPoolSize=pullSize,
            waitQueueMultiple=10,
            waitQueueTimeoutMS=1000
        )
    return connection


def get_mongo_db(db_name):
    return get_connection()[db_name]


def get_utair_db():
    return get_mongo_db(config.MONGODB_SETTINGS.get('DB'))
