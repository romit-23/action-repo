from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongodb:27017/")
db = client.github_events

@app.route("/events", methods=["GET"])
def get_events():
    events = list(db.events.find().sort("timestamp", -1).limit(10))
    return jsonify(events)
@app.route("/webhook", methods=["POST"])
def webhook():
    payload = request.json
    event = request.headers.get("X-GitHub-Event")

    if event == "push":
        doc = {
            "author": payload["pusher"]["name"],
            "action": "PUSH",
            "to_branch": payload["ref"].split("/")[-1],
            "timestamp": payload["head_commit"]["timestamp"],
        }
    elif event == "pull_request":
        doc = {
            "author": payload["pull_request"]["user"]["login"],
            "action": "PULL_REQUEST",
            "from_branch": payload["pull_request"]["head"]["ref"],
            "to_branch": payload["pull_request"]["base"]["ref"],
            "timestamp": payload["pull_request"]["updated_at"],
        }
    elif event == "merge":
        doc = {
            "author": payload["sender"]["login"],
            "action": "MERGE",
            "from_branch": payload["pull_request"]["head"]["ref"],
            "to_branch": payload["pull_request"]["base"]["ref"],
            "timestamp": payload["pull_request"]["merged_at"],
        }
    else:
        return jsonify({"status": "ignored"}), 200

    db.events.insert_one(doc)
    return jsonify({"status": "success"}), 200