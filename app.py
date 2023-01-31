from flask import Flask, request
from util import get_all_reminders

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"
# find all reminders
@app.route("/reminder/all", methods=['GET'])
def get_all():
    reminders = get_all_reminders()
    return reminders

# find all reminders today
# @app.route("/reminder/today", methods=['GET'])
# def get_today():

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
