from flask import Flask, request
from util import get_all_reminders

app = Flask(__name__)

# find all reminders
@app.route("/reminder/all", methods=['GET'])
def get_all():
    reminders = get_all_reminders()
    return reminders

# find all reminders today
@app.route("/reminder/today", methods=['GET'])
def get_today():

