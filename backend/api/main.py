import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

from lib.list import Task, List
from lib.auth import Session
from lib.user import User

import random

# create a Flask app with cors enabled
app = Flask(__name__)
CORS(app)


@app.route('/auth/validate', methods=['POST'])
def auth_validate():

    session_token = request.json['session_token']

    # connect to "data.db" database with sqlite
    conn = sqlite3.connect('data.db')

    [validated, message, data] = Session.verifyToken(session_token, conn)

    # close the connection
    conn.close()

    return jsonify({
        "validated": validated,
        "message": message,
        "data": {
            "user": {
                "user_id": data.user_id,
                "user_name": data.user_name,
                "user_email": data.user_email,
                "user_color": data.user_color
            } if data != None else None
        }
    })


@app.route('/auth/login', methods=['POST'])
def auth_login():
    user_email = request.json['email']
    user_password = request.json['password']

    conn = sqlite3.connect('data.db')

    c = conn.cursor()

    user = User.getUserByEmail(user_email, conn)

    if user == None:
        return jsonify({
            "validated": False,
            "message": "User not found",
            "data": None})

    if user.user_password != user_password:
        return jsonify({"validated": False, "message": "Wrong password", "data": None})

    [token, _] = Session.createSession(user.user_id, conn)

    conn.close()

    # add session token to cookies

    return jsonify({"validated": True, "message": "User authentified", "data": {
        "user": {
            "user_id": user.user_id,
            "user_name": user.user_name,
            "user_email": user.user_email,
            "user_color": user.user_color
        },
        "session_token": token
    }})


@app.route('/auth/logout', methods=['POST'])
def auth_logout():
    session_token = request.json['session_token']

    conn = sqlite3.connect('data.db')

    c = conn.cursor()

    c.execute("DELETE FROM Session WHERE session_token = ?", (session_token,))

    conn.close()

    return jsonify({"validated": True, "message": "User logged out", "data": None})


@app.route('/auth/signup', methods=['POST'])
def auth_signup():
    user_name = request.json['name']
    user_email = request.json['email']
    user_password = request.json['password']

    conn = sqlite3.connect('data.db')

    c = conn.cursor()

    user = User.getUserByEmail(user_email, conn)

    if user != None:
        return jsonify({"validated": False, "message": "User already exists", "data": None})

    user_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    
    user = User.createUser(user_name, user_email, user_password, user_color, conn)

    [token, _] = Session.createSession(user.user_id, conn)

    conn.close()

    return jsonify({"validated": True, "message": "User authentified", "data": {
        "user": {
            "user_id": user.user_id,
            "user_name": user.user_name,
            "user_email": user.user_email,
            "user_color": user.user_color
        },
        "session_token": token
    }})


@app.route('/tasks', methods=['DELETE'])
def tasks_delete():
    session_token = request.json['session_token']
    task_id = request.json['task_id']

    conn = sqlite3.connect('data.db')

    [validated, message, user] = Session.verifyToken(session_token, conn)

    if not validated:
        return jsonify({"validated": False, "message": message, "data": None})

    Task.removeTask(task_id, conn)

    conn.close()

    return jsonify({"validated": True, "message": "Task deleted", "data": None})


@app.route('/lists', methods=['DELETE'])
def lists_delete():
    session_token = request.json['session_token']
    list_id = request.json['list_id']

    conn = sqlite3.connect('data.db')

    [validated, message, user] = Session.verifyToken(session_token, conn)

    if not validated:
        return jsonify({"validated": False, "message": message, "data": None})

    List.removeList(list_id, conn)

    conn.close()

    return jsonify({"validated": True, "message": "List deleted", "data": None})


@app.route('/tasks/move', methods=['PUT'])
def tasks_move():
    session_token = request.json['session_token']
    task_id = request.json['task_id']
    list_id = request.json['list_id']

    conn = sqlite3.connect('data.db')

    [validated, message, user] = Session.verifyToken(session_token, conn)

    if not validated:
        return jsonify({"validated": False, "message": message, "data": None})

    task = Task.getTask(task_id, conn)

    task.updateTaskList(list_id, conn)

    conn.close()

    return jsonify({"validated": True, "message": "Task moved", "data": None})


@app.route('/tasks/assign', methods=['PUT'])
def tasks_assign():
    session_token = request.json['session_token']
    task_id = request.json['task_id']
    user_id = request.json['user_id']

    conn = sqlite3.connect('data.db')

    [validated, message, user] = Session.verifyToken(session_token, conn)

    if not validated:
        return jsonify({"validated": False, "message": message, "data": None})

    task = Task.getTask(task_id, conn)

    task.updateTaskUser(user_id, conn)

    conn.close()

    return jsonify({"validated": True, "message": "Task assigned", "data": None})


@app.route('/tasks/create', methods=['POST'])
def tasks_create():
    session_token = request.json['session_token']
    list_id = request.json['list_id']
    task_title = request.json['task_name']
    user_id = request.json['user_id']

    print(session_token, list_id, task_title, user_id)

    conn = sqlite3.connect('data.db')

    [validated, message, user] = Session.verifyToken(session_token, conn)

    if not validated:
        return jsonify({"validated": False, "message": message, "data": None})

    task = Task.createTask(list_id, user_id, task_title, conn)

    conn.close()

    return jsonify({"validated": True, "message": "Task created", "data": {
        "task_id": task.task_id,
        "task_title": task.task_title,
        "task_list_id": task.list_id,
        "task_user_id": task.user_id
    }})


@app.route('/lists', methods=['POST'])
def tasks_get():
    session_token = request.json['session_token']

    conn = sqlite3.connect('data.db')

    [validated, message, user] = Session.verifyToken(session_token, conn)

    if not validated:
        return jsonify({"validated": False, "message": message, "data": None})

    lists = List.getLists(conn)

    for list in lists:
        list.tasks = Task.getTasks(list.list_id, conn)
        print(list.list_id)
        print(list.list_title)
        print([task.task_title for task in list.tasks])

    conn.close()

    return jsonify({
        "validated": True,
        "message": "Tasks fetched",
        "data": {
            "lists": [{
                "list_id": list.list_id,
                "list_title": list.list_title,
                "tasks": [{
                    "task_id": task.task_id,
                    "task_title": task.task_title,
                    "user_id": task.user_id,
                    "user_name": task.user_name,
                    "user_color": task.user_color,
                } for task in list.tasks]
            } for list in lists]
        }
    })


@app.route('/lists/create', methods=['POST'])
def lists_create():
    session_token = request.json['session_token']
    list_title = request.json['list_title']

    conn = sqlite3.connect('data.db')

    [validated, message, user] = Session.verifyToken(session_token, conn)

    if not validated:
        return jsonify({"validated": False, "message": message, "data": None})

    list = List.createList(list_title, conn)

    conn.close()

    return jsonify({"validated": True, "message": "List created", "data": {
        "list_id": list.list_id,
        "list_title": list.list_title
    }})


@app.route('/users', methods=['POST'])
def users_get():

    session_token = request.json['session_token']

    conn = sqlite3.connect('data.db')

    [validated, message, user] = Session.verifyToken(session_token, conn)

    if not validated:
        return jsonify({"validated": False, "message": message, "data": None})

    conn = sqlite3.connect('data.db')

    users = User.getUsers(conn)

    conn.close()

    return jsonify({
        "validated": True,
        "message": "Users fetched",
        "data": {
            "users": [{
                "user_id": user.user_id,
                "user_name": user.user_name,
                "user_email": user.user_email,
                "user_color": user.user_color
            } for user in users]
        }
    })
