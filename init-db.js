db = db.getSiblingDB("reminder_db");
db.reminder.drop();

const d = new Date('August 19, 1975 23:15:30 UTC');

const jsonDate = d.toJSON();

db.reminder.insertMany([
    {
        "done": false,
        "todo": "eat apple",
        "date": jsonDate
    }
])