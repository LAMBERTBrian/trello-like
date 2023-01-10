class List:
    def __init__(self, list_id, team_id, list_title):
        self.list_id = list_id
        self.team_id = team_id
        self.list_title = list_title

class Task:
    def __init__(self, task_id, list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at):
        self.task_id = task_id
        self.list_id = list_id
        self.user_id = user_id
        self.task_title = task_title
        self.task_state = task_state
        self.task_created_at = task_created_at
        self.task_starts_at = task_starts_at
        self.task_ends_at = task_ends_at

class Comment:
    def __init__(self, comment_id, task_id, created_at, title, body):
        self.comment_id = comment_id
        self.task_id = task_id
        self.created_at = created_at
        self.title = title
        self.body = body