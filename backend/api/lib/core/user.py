class User:
    def __init__(self, user_id, user_name, user_email, user_password):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password

    @staticmethod
    def getUser(user_id, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM User WHERE user_id = %s", (user_id,))
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
        cur.execute("INSERT INTO User (user_name, user_email, user_password) VALUES (%s, %s, %s)", (user_name, user_email, user_password))
        conn.commit()
        cur.execute("SELECT * FROM User WHERE user_name = %s", (user_name,))
        [user_id, user_name, user_email, user_password] = cur.fetchone()
        user = User(user_id, user_name, user_email, user_password)
        return user

    @staticmethod
    def deleteUser(user_id, conn):
        cur = conn.cursor()
        cur.execute("DELETE FROM User WHERE user_id = %s", (user_id,))
        conn.commit()

    def updateUserName(self, user_name, conn):
        cur = conn.cursor()
        cur.execute("UPDATE User SET user_name = %s WHERE user_id = %s", (user_name, self.user_id))
        conn.commit()
        self.user_name = user_name

    def updateUserEmail(self, user_email, conn):
        cur = conn.cursor()
        cur.execute("UPDATE User SET user_email = %s WHERE user_id = %s", (user_email, self.user_id))
        conn.commit()
        self.user_email = user_email

    def updateUserPassword(self, user_password, conn):
        cur = conn.cursor()
        cur.execute("UPDATE User SET user_password = %s WHERE user_id = %s", (user_password, self.user_id))
        conn.commit()
        self.user_password = user_password