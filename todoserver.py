#todoserver.py

from flask import Flask, make_response, request
import json

app = Flask(__name__)

# cheat to test database lookup
MEMORY = {}

@app.route("/tasks/", methods=["GET"])
def get_all_tasks():
    return make_response("[]", 200)

@app.route("/tasks/", methods=["POST"])
def create_task():
    payload = request.get_json(force=True)
    task_id = 1
    MEMORY[task_id] = {
        "summary": payload["summary"],
        "description": payload["description"],
    }
    task_info = {"id": task_id}
    return make_response(json.dumps(task_info), 201)

@app.route("/tasks/<int:task_id>/")
def task_details(task_id):
    task_info = MEMORY[task_id].copy()
    task_info["id"] = task_id
    return json.dumps(task_info)

if __name__ == "__main__":
    app.run()