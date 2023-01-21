import json


class List:
    def __init__(self, list_id, list_title):
        self.list_id = list_id
        self.list_title = list_title

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def getLists(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM List")
        lists = [List(list_id, list_title)
                 for list_id, list_title in cur.fetchall()]
        return lists

    @staticmethod
    def getList(list_id, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM List WHERE list_id = ?", (list_id,))
        raw_data = cur.fetchone()
        if list_id is None:
            return None
        [list_id, list_title] = raw_data
        list = List(list_id, list_title)
        return list

    @staticmethod
    def createList(list_title, conn):
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO List (list_title) VALUES (?)", (list_title,))
        conn.commit()
        cur.execute(
            "SELECT * FROM List WHERE list_title = ?", (list_title,))
        [list_id, list_title] = cur.fetchone()
        list = List(list_id, list_title)
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
        lists = [List(list_id, list_title)
                 for list_id, list_title in cur.fetchall()]
        return lists

    def updateListTitle(self, list_title, conn):
        cur = conn.cursor()
        cur.execute("UPDATE List SET list_title = ? WHERE list_id = ?",
                    (list_title, self.list_id))
        conn.commit()
        self.list_title = list_title


class Task:
    def __init__(self, task_id, list_id, user_id, task_title, user_name, user_color):
        self.task_id = task_id
        self.list_id = list_id
        self.user_id = user_id
        self.task_title = task_title
        self.user_name = user_name
        self.user_color = user_color

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def getTask(task_id, conn):
        cur = conn.cursor()
        # get task and user name of user id in task
        cur.execute(
            "SELECT Task.task_id, Task.list_id, Task.user_id, Task.task_title, User.user_name, User.user_color FROM Task INNER JOIN User ON Task.user_id = User.user_id WHERE Task.task_id = ?", (task_id,))
        [task_id, list_id, user_id, task_title,
            user_name, user_color] = cur.fetchone()
        task = Task(task_id, list_id, user_id,
                    task_title, user_name, user_color)
        return task

    @staticmethod
    def getTasks(list_id, conn):
        cur = conn.cursor()
        cur.execute(
            "SELECT Task.task_id, Task.list_id, Task.user_id, Task.task_title, User.user_name, User.user_color FROM Task INNER JOIN User ON Task.user_id = User.user_id WHERE Task.list_id = ?", (list_id,))

        tasks = [Task(task_id, list_id, user_id, task_title, user_name, user_color)
                 for task_id, list_id, user_id, task_title, user_name, user_color in cur.fetchall()]

        return tasks

    @staticmethod
    def createTask(list_id, user_id, task_title, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO Task (list_id, user_id, task_title) VALUES (?, ?, ?)",
                    (list_id, user_id, task_title))
        conn.commit()
        # get task and user name of user id in task
        cur.execute(
            "SELECT Task.task_id, Task.list_id, Task.user_id, Task.task_title, User.user_name, User.user_color FROM Task INNER JOIN User ON Task.user_id = User.user_id WHERE Task.list_id = ? AND Task.user_id = ? AND Task.task_title = ?", (list_id, user_id, task_title))
        [task_id, list_id, user_id, task_title,
            user_name, user_color] = cur.fetchone()
        task = Task(task_id, list_id, user_id,
                    task_title, user_name, user_color)
        return task

    @staticmethod
    def removeTask(task_id, conn):
        cur = conn.cursor()
        cur.execute("DELETE FROM Task WHERE task_id = ?", (task_id,))
        conn.commit()

    def updateTaskTitle(self, task_title, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Task SET task_title = ? WHERE task_id = ?",
                    (task_title, self.task_id))
        conn.commit()
        self.task_title = task_title

    def updateTaskUser(self, user_id, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Task SET user_id = ? WHERE task_id = ?",
                    (user_id, self.task_id))
        conn.commit()
        self.user_id = user_id

    def updateTaskList(self, list_id, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Task SET list_id = ? WHERE task_id = ?",
                    (list_id, self.task_id))
        conn.commit()
        self.list_id = list_id
