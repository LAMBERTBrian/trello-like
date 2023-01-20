from time import time
import secrets
from user import User

class Session:
    def __init__(self, user_id, session_token, session_exp):
        self.user_id = user_id
        self.session_token = session_token
        self.session_exp = session_exp

    @staticmethod
    def verifyToken(session_token, conn):
        c = conn.cursor()
        now = time.now()
        c.execute("SELECT * FROM Session WHERE session_token = ? AND session_exp > ? ", (session_token, now))
        session = [Session(user_id, session_token, session_exp) for user_id, session_token, session_exp in c.fetchall()][0]

        if session == None:
            return (False, "User not found", None)

        user = User.getUser(session.user_id)

        return (False, "User authentified", user)

    @staticmethod
    def createSession(user_id, conn):
        exp = time.now() + 24 * 3600
        token = secrets.token_hex(16)
        c = conn.cursor()
        c.execute('INSERT INTO Session (user_id, session_token, session_exp) VALUES (?, ?, ?)', (user_id, token, exp))
        c.commit()
        return token