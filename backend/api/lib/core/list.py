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

    @staticmethod
    def getTask(task_id, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Task WHERE task_id = %s", (task_id,))
        [task_id, list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at] = cur.fetchone()
        task = Task(task_id, list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at)
        return task

    @staticmethod
    def getTasks(list_id, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Task WHERE list_id = %s", (list_id,))
        tasks = [Task(task_id, list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at) for task_id,list_id,user_id,task_title,task_state,task_created_at,task_starts_at,task_ends_at in cur.fetchall()]
        return tasks

    @staticmethod
    def createTask(list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO Task (list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at) VALUES (%s, %s, %s, %s, %s, %s, %s)", (list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at))
        conn.commit()
        cur.execute("SELECT * FROM Task WHERE list_id = %s AND user_id = %s AND task_title = %s AND task_state = %s AND task_created_at = %s AND task_starts_at = %s AND task_ends_at = %s", (list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at))
        [task_id, list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at] = cur.fetchone()
        task = Task(task_id, list_id, user_id, task_title, task_state, task_created_at, task_starts_at, task_ends_at)
        return task

    @staticmethod
    def removeTask(task_id, conn):
        cur = conn.cursor()
        cur.execute("DELETE FROM Task WHERE task_id = %s", (task_id,))
        conn.commit()
    
    def updateTaskTitle(self, task_title, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Task SET task_title = %s WHERE task_id = %s", (task_title, self.task_id))
        conn.commit()
        self.task_title = task_title

    def updateTaskState(self, task_state, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Task SET task_state = %s WHERE task_id = %s", (task_state, self.task_id))
        conn.commit()
        self.task_state = task_state

    def updateTaskStartsAt(self, task_starts_at, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Task SET task_starts_at = %s WHERE task_id = %s", (task_starts_at, self.task_id))
        conn.commit()
        self.task_starts_at = task_starts_at

    def updateTaskEndsAt(self, task_ends_at, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Task SET task_ends_at = %s WHERE task_id = %s", (task_ends_at, self.task_id))
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

    def updateCommentTitle(self, title, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Comment SET title = %s WHERE comment_id = %s", (title, self.comment_id))
        conn.commit()
        self.title = title

    def updateCommentBody(self, body, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Comment SET body = %s WHERE comment_id = %s", (body, self.comment_id))
        conn.commit()
        self.body = body