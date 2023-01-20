import sqlite3
from flask import Flask, jsonify

from lib.list import Task
from lib.team import Team

app = Flask(__name__)

# get team

@app.route('/team/<team_id>')
def get_team_by_id(team_id):
    conn = sqlite3.connect('data.db')

    team = Team.getTeam(team_id, conn)

    team_json = team.toJson()    

    return jsonify(team_json)

# get lists
# get tasks
# get list
# get task
# get members
# get member
# get comments
# get comment


@app.route('/user/<username>')
def get_user_email(username):
    # connect to "data.db" database with sqlite
    conn = sqlite3.connect('data.db')

    # create a cursor object
    c = conn.cursor()

    # execute a query
    c.execute("SELECT * FROM User WHERE user_name = ?", (username,))

    # fetch the result
    user = c.fetchone()

    # close the connection
    conn.close()

    # return the result
    return str(user)

# api route that get user's membership status
@app.route('/user/<username>/team')
def get_user_membership(username):
    # connect to "data.db" database with sqlite
    conn = sqlite3.connect('data.db')

    # create a cursor object
    c = conn.cursor()

    # execute a query that gets all the teams of the user by finding all the foreign keys in the Member table
    c.execute("SELECT team_name FROM Team WHERE team_id = (SELECT team_id FROM Member WHERE user_id = (SELECT user_id FROM User WHERE user_name = ?))", (str(username),))

    # fetch the result
    data = c.fetchall()

    # close the connection
    conn.close()

    # return the result
    return str(data)

# api route that change the state of a task
@app.route('/task/<task_id>/set-state/<state>')
def set_task_state(task_id, state):
    # connect to "data.db" database with sqlite
    conn = sqlite3.connect('data.db')

    task = Task.getTask(task_id, conn)

    task.updateTaskState(state, conn)

    # close the connection
    conn.close()

    # return the result
    return "success"



# api route that get all members of a team with their role and name
@app.route('/team/<team_name>/members')
def get_team_members(team_name):
    # connect to "data.db" database with sqlite
    conn = sqlite3.connect('data.db')

    # create a cursor object
    c = conn.cursor()

    # join the Member and User tables to get the user_name and member_role
    c.execute("SELECT user_name, member_role FROM User JOIN Member ON User.user_id = Member.user_id WHERE team_id = (SELECT team_id FROM Team WHERE team_name = ?)", (team_name,))

    # fetch the result
    data = c.fetchall()

    # close the connection
    conn.close()

    # return the result
    return str(data)

@app.route('/debug/populate_db') # this is for debugging purposes only
def populate_db():
    # connect to "data.db" database with sqlite
    conn = sqlite3.connect('data.db')

    # create a cursor object

    c = conn.cursor()

    # clear the database
    c.execute('DELETE FROM User')
    
    c.execute('DELETE FROM Team')
    
    c.execute('DELETE FROM Member')
    
    c.execute('DELETE FROM List')
    
    c.execute('DELETE FROM Task')
    
    c.execute('DELETE FROM Comment')
    

    c.execute('INSERT INTO User (user_name, user_email, user_password) VALUES("Kelliananas", "a@gmail.com", "Cznzijeyèé2Y28J82J")')
    
    c.execute('INSERT INTO User (user_name, user_email, user_password) VALUES("Kokoriko", "arobase@sfr.com", "gzydjbcat103836426GTRFEDEZCS")')
    
    c.execute('INSERT INTO User (user_name, user_email, user_password) VALUES("Ktzerfsd123", "rgzsfd@saintaubinlasalle.fr", "XX_UIT_123")')
    
    c.execute('INSERT INTO User (user_name, user_email, user_password) VALUES("UIO", "fsdfz@b.com", "fraise3214")')
    
    c.execute('INSERT INTO User (user_name, user_email, user_password) VALUES("45", "efsd@hotmail.com", "Canardboiteux")')
    
    c.execute('INSERT INTO Team (team_name) VALUES("Kelliananas")')
    
    c.execute('INSERT INTO Team (team_name) VALUES("GroupeA")')
    

    c.execute('INSERT INTO Member (user_id, team_id, member_role) VALUES(1, 1, "admistrator")')
    
    c.execute('INSERT INTO Member (user_id, team_id, member_role) VALUES(2, 1, "member")')
    
    c.execute('INSERT INTO Member (user_id, team_id, member_role) VALUES(3, 2, "member")')
    
    c.execute('INSERT INTO Member (user_id, team_id, member_role) VALUES(4, 1, "member")')
    
    c.execute('INSERT INTO Member (user_id, team_id, member_role) VALUES(5, 2, "administrator")')
    

    c.execute('INSERT INTO List (team_id, list_title) VALUES(1, "To do")')
    
    c.execute('INSERT INTO List (team_id, list_title) VALUES(1, "Done")')
    
    c.execute('INSERT INTO List (team_id, list_title) VALUES(1, "Abandonned")')
    
    c.execute('INSERT INTO List (team_id, list_title) VALUES(2, "To do")')
    
    c.execute('INSERT INTO List (team_id, list_title) VALUES(2, "Done")')
    
    c.execute('INSERT INTO List (team_id, list_title) VALUES(2, "Abandonned")')
    

    c.execute('INSERT INTO Task (list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at) VALUES(1, 1, "Faire la vaisselle", "To do", "16/11/2022", "04/12/2022", "29/12/2023")')
    
    c.execute('INSERT INTO Task (list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at) VALUES(2, 2, "Manger du pain", "Done", "12/12/2020", "12/12/2020", "29/12/2023")')
    
    c.execute('INSERT INTO Task (list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at) VALUES(6, 3, "Faire du sport", "Abandonned", "16/11/2022", "29/12/2023", "29/12/2023")')
    

    c.execute('INSERT INTO Comment (task_id, user_id, comment_created_at, comment_title, comment_body) VALUES(1, 2, "25/11/2022", "RAPPEL", "Commence la tache!")')
    
    c.execute('INSERT INTO Comment (task_id, user_id, comment_created_at, comment_title, comment_body) VALUES(2, 2, "25/11/2022", "FAIT", "On a fini cette tâche.")')
    
    c.execute('INSERT INTO Comment (task_id, user_id, comment_created_at, comment_title, comment_body) VALUES(3, 5, "12/09/2024", "ANNULATION TACHE", "On annule cet tache ")')
    
    conn.commit()

    conn.close()

    return "Database populated"