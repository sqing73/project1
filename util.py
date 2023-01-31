import pymongo
from pymongo import MongoClient

client = MongoClient(host="test_mongodb",
                       port=27017,
)
                    #    username="root",
                    #    password="pass",
                    #    authsource="admin")

db = client["reminder_db"]

col = db["reminder"]

def get_all_reminders():
    reminders = col.find({}, {"_id":0})
    return list(reminders)