#todoserver\app.py

import json

from flask import (
    Flask,
    make_response,
    request,
)

from .store import TaskStore

class TodoserverApp(Flask):
    def init_db(self, engine_spec):
        self.store = TaskStore(engine_spec)

    def erase_all_test_data(self):
        assert self.testing # if true, TEST MODE; otherwise PROD MODE *BOMB*
        self.store._delete_all_tasks()
        
app = TodoserverApp(__name__)

@app.route("/tasks/", methods=["GET"])
def get_all_tasks():
    tasks = app.store.get_all_tasks()
    return make_response(json.dumps(tasks), 200)

@app.route("/tasks/", methods=["POST"])
def create_task():
    payload = request.get_json(force=True)
    task_id = app.store.create_task(
        summary = payload["summary"],
        description = payload["description"],
    )
    task_info = {"id": task_id}
    return make_response(json.dumps(task_info), 201)

@app.route("/tasks/<int:task_id>/")
def task_details(task_id):
    task_info = app.store.task_details(task_id)
    return json.dumps(task_info)
