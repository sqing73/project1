import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]

mycol = mydb["reminder"]

def get_all_reminders():
    reminders = mycol.find({}, {"_id":0})
    return list(reminders)