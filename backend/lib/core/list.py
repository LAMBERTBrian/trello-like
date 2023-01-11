class List:
    def __init__(self, list_id, team_id, list_title):
        self.list_id = list_id
        self.team_id = team_id
        self.list_title = list_title

    @staticmethod
    def getList(list_id, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM List WHERE list_id = %s", (list_id,))
        [list_id, team_id, list_title] = cur.fetchone()
        list = List(list_id, team_id, list_title)
        return list

    @staticmethod
    def createList(team_id, list_title, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO List (team_id, list_title) VALUES (%s, %s)", (team_id, list_title))
        conn.commit()
        cur.execute("SELECT * FROM List WHERE team_id = %s AND list_title = %s", (team_id, list_title))
        [list_id, team_id, list_title] = cur.fetchone()
        list = List(list_id, team_id, list_title)
        return list

    @staticmethod
    def removeList(list_id, conn):
        cur = conn.cursor()
        cur.execute("DELETE FROM List WHERE list_id = %s", (list_id,))
        conn.commit()

    @staticmethod
    def getLists(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM List")
        lists = [List(list_id, team_id, list_title) for list_id,team_id,list_title in cur.fetchall()]
        return lists

    def updateListTitle(self, list_title, conn):
        cur = conn.cursor()
        cur.execute("UPDATE List SET list_title = %s WHERE list_id = %s", (list_title, self.list_id))
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

class Comment:
    def __init__(self, comment_id, task_id, created_at, title, body):
        self.comment_id = comment_id
        self.task_id = task_id
        self.created_at = created_at
        self.title = title
        self.body = body

    @staticmethod
    def getComment(comment_id, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Comment WHERE comment_id = %s", (comment_id,))
        [comment_id, task_id, created_at, title, body] = cur.fetchone()
        comment = Comment(comment_id, task_id, created_at, title, body)
        return comment

    @staticmethod
    def getComments(task_id, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Comment WHERE task_id = %s", (task_id,))
        comments = [Comment(comment_id, task_id, created_at, title, body) for comment_id,task_id,created_at,title,body in cur.fetchall()]
        return comments

    @staticmethod
    def createComment(task_id, title, body, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO Comment (task_id, title, body) VALUES (%s, %s, %s)", (task_id, title, body))
        conn.commit()
        cur.execute("SELECT * FROM Comment WHERE task_id = %s AND title = %s AND body = %s", (task_id, title, body))
        [comment_id, task_id, created_at, title, body] = cur.fetchone()
        comment = Comment(comment_id, task_id, created_at, title, body)
        return comment

    @staticmethod
    def removeComment(comment_id, conn):
        cur = conn.cursor()
        cur.execute("DELETE FROM Comment WHERE comment_id = %s", (comment_id,))
        conn.commit()

    def updateComment(self, title, body, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Comment SET title = %s, body = %s WHERE comment_id = %s", (title, body, self.comment_id))
        conn.commit()
        self.title = title
        self.body = body