from flask import Flask, request
import pymongo, os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGODB_URI")

# Connect to MongoDB
client = pymongo.MongoClient(uri)
db = client["todo_db"]
collection = db["to-do_tasks"]

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_task():
    task = request.get_json()
    collection.insert_one(task)
    return "Task submitted successfully!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = list(collection.find({}, {'_id': 0}))
    return {"tasks": tasks}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)