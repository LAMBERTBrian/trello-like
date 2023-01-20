import json


class User:
    def __init__(self, user_id, user_name, user_email, user_password):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def getUser(user_id, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM User WHERE user_id = ?", (user_id,))
        [user_id, user_name, user_email, user_password] = cur.fetchone()
        user = User(user_id, user_name, user_email, user_password)
        return user

    @staticmethod
    def getUsers(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM User")
        users = [User(user_id, user_name, user_email, user_password) for user_id,user_name,user_email,user_password in cur.fetchall()]
        return users

    @staticmethod
    def createUser(user_name, user_email, user_password, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO User (user_name, user_email, user_password) VALUES (?, ?, ?)", (user_name, user_email, user_password))
        conn.commit()
        cur.execute("SELECT * FROM User WHERE user_name = ?", (user_name,))
        [user_id, user_name, user_email, user_password] = cur.fetchone()
        user = User(user_id, user_name, user_email, user_password)
        return user

    @staticmethod
    def deleteUser(user_id, conn):
        cur = conn.cursor()
        cur.execute("DELETE FROM User WHERE user_id = ?", (user_id,))
        conn.commit()

    def updateUserName(self, user_name, conn):
        cur = conn.cursor()
        cur.execute("UPDATE User SET user_name = ? WHERE user_id = ?", (user_name, self.user_id))
        conn.commit()
        self.user_name = user_name

    def updateUserEmail(self, user_email, conn):
        cur = conn.cursor()
        cur.execute("UPDATE User SET user_email = ? WHERE user_id = ?", (user_email, self.user_id))
        conn.commit()
        self.user_email = user_email

    def updateUserPassword(self, user_password, conn):
        cur = conn.cursor()
        cur.execute("UPDATE User SET user_password = ? WHERE user_id = ?", (user_password, self.user_id))
        conn.commit()
        self.user_password = user_password