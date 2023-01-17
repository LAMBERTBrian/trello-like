import json


class List:
    def __init__(self, list_id, team_id, list_title):
        self.list_id = list_id
        self.team_id = team_id
        self.list_title = list_title

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def getList(list_id, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM List WHERE list_id = ?", (list_id,))
        [list_id, team_id, list_title] = cur.fetchone()
        list = List(list_id, team_id, list_title)
        return list

    @staticmethod
    def createList(team_id, list_title, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO List (team_id, list_title) VALUES (?, ?)", (team_id, list_title))
        conn.commit()
        cur.execute("SELECT * FROM List WHERE team_id = ? AND list_title = ?", (team_id, list_title))
        [list_id, team_id, list_title] = cur.fetchone()
        list = List(list_id, team_id, list_title)
        return list

    @staticmethod
    def removeList(list_id, conn):
        cur = conn.cursor()
        cur.execute("DELETE FROM List WHERE list_id = ?", (list_id,))
        conn.commit()

    @staticmethod
    def getLists(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM List")
        lists = [List(list_id, team_id, list_title) for list_id,team_id,list_title in cur.fetchall()]
        return lists

    def updateListTitle(self, list_title, conn):
        cur = conn.cursor()
        cur.execute("UPDATE List SET list_title = ? WHERE list_id = ?", (list_title, self.list_id))
        conn.commit()
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

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def getTask(task_id, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Task WHERE task_id = ?", (task_id,))
        [task_id, list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at] = cur.fetchone()
        task = Task(task_id, list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at)
        return task

    @staticmethod
    def getTasks(list_id, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Task WHERE list_id = ?", (list_id,))
        tasks = [Task(task_id, list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at) for task_id,list_id,user_id,task_title,task_state,task_created_at,task_starts_at,task_ends_at in cur.fetchall()]
        return tasks

    @staticmethod
    def createTask(list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO Task (list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at) VALUES (?, ?, ?, ?, ?, ?, ?)", (list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at))
        conn.commit()
        cur.execute("SELECT * FROM Task WHERE list_id = ? AND user_id = ? AND task_title = ? AND task_state = ? AND task_created_at = ? AND task_starts_at = ? AND task_ends_at = ?", (list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at))
        [task_id, list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at] = cur.fetchone()
        task = Task(task_id, list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at)
        return task

    @staticmethod
    def removeTask(task_id, conn):
        cur = conn.cursor()
        cur.execute("DELETE FROM Task WHERE task_id = ?", (task_id,))
        conn.commit()
    
    def updateTaskTitle(self, task_title, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Task SET task_title = ? WHERE task_id = ?", (task_title, self.task_id))
        conn.commit()
        self.task_title = task_title

    def updateTaskState(self, task_state, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Task SET task_state = ? WHERE task_id = ?", (task_state, self.task_id))
        conn.commit()
        self.task_state = task_state

    def updateTaskStartsAt(self, task_starts_at, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Task SET task_starts_at = ? WHERE task_id = ?", (task_starts_at, self.task_id))
        conn.commit()
        self.task_starts_at = task_starts_at

    def updateTaskEndsAt(self, task_ends_at, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Task SET task_ends_at = ? WHERE task_id = ?", (task_ends_at, self.task_id))
        conn.commit()
        self.task_ends_at = task_ends_at

class Comment:
    def __init__(self, comment_id, user_id, task_id, created_at, title, body):
        self.comment_id = comment_id
        self.user_id = user_id
        self.task_id = task_id
        self.created_at = created_at
        self.title = title
        self.body = body

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def getComment(comment_id, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Comment WHERE comment_id = ?", (comment_id,))
        [comment_id, task_id, created_at, title, body] = cur.fetchone()
        comment = Comment(comment_id, task_id, created_at, title, body)
        return comment

    @staticmethod
    def getComments(task_id, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Comment WHERE task_id = ?", (task_id,))
        comments = [Comment(comment_id, task_id, created_at, title, body) for comment_id,task_id,created_at,title,body in cur.fetchall()]
        return comments

    @staticmethod
    def createComment(task_id, title, body, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO Comment (task_id, title, body) VALUES (?, ?, ?)", (task_id, title, body))
        conn.commit()
        cur.execute("SELECT * FROM Comment WHERE task_id = ? AND title = ? AND body = ?", (task_id, title, body))
        [comment_id, task_id, created_at, title, body] = cur.fetchone()
        comment = Comment(comment_id, task_id, created_at, title, body)
        return comment

    @staticmethod
    def removeComment(comment_id, conn):
        cur = conn.cursor()
        cur.execute("DELETE FROM Comment WHERE comment_id = ?", (comment_id,))
        conn.commit()

    def updateCommentTitle(self, title, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Comment SET title = ? WHERE comment_id = ?", (title, self.comment_id))
        conn.commit()
        self.title = title

    def updateCommentBody(self, body, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Comment SET body = ? WHERE comment_id = ?", (body, self.comment_id))
        conn.commit()
        self.body = body