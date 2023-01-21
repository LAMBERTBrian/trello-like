from time import time
import secrets
from lib.user import User


class Session:
    def __init__(self, user_id, session_token, session_exp):
        self.user_id = user_id
        self.session_token = session_token
        self.session_exp = session_exp

    @staticmethod
    def verifyToken(session_token, conn):
        c = conn.cursor()
        now = time()
        c.execute(
            "SELECT * FROM Session WHERE session_token = ? AND session_exp > ? ", (session_token, now))

        raw_session = c.fetchone()

        if not raw_session:
            return (False, "Session expired or not found", None)

        [user_id, session_token, session_exp] = raw_session

        session = Session(user_id, session_token, session_exp)

        user = User.getUser(session.user_id, conn)

        if not user:
            return (False, "User not found", None)

        return (True, "Session verified", user)

    @staticmethod
    def createSession(user_id, conn):
        exp = time() + 24 * 3600
        token = secrets.token_hex(16)
        c = conn.cursor()
        c.execute(
            'INSERT INTO Session (user_id, session_token, session_exp) VALUES (?, ?, ?)', (user_id, token, exp))
        conn.commit()
        return [token, exp]
