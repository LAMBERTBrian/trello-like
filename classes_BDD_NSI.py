class User:
    def __init__(self, user_id, user_name, user_email, user_password):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password

class Member:
    def __init__(self, user_id, team_id, role):
        self.user_id = user_id
        self.team_id = team_id
        self.role = role

class Team:
    def __init__(self, team_id, team_name):
        self.team_id = team_id 
        self.team_namename = team_name

class List:
    def __init__(self, list_id, team_id, list_title):
        self.team_id = team_id
        self.list_id = list_id 
        self.list_title = list_title

class Task:
    def __init__(self, task_id, list_id, team_id, user_id, task_title, state, created_at, starts_at, ends_at):
        self.task_id = task_id
        self.list_id = list_id
        self.team_id = team_id
        self.user_id = user_id
        self.task_title = task_title 
        self.state = state
        self.created_at = created_at
        self.starts_at = starts_at
        self.ends_at = ends_at

class Comment:
    def __init__(self, comment_id, task_id, user_id, created_at, title, body):
        self.comment_id = comment_id
        self.task_id = task_id
        self.user_id = user_id
        self.created_at = created_at
        self.title = title
        self.body = body







