class Team:
    def __init__(self, team_id, team_name):
        self.team_id = team_id
        self.team_name = team_name

    @staticmethod
    def getTeam(team_id, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Team WHERE team_id = %s", (team_id,))
        [team_id, team_name] = cur.fetchone()
        team = Team(team_id, team_name)
        return team

    @staticmethod
    def getTeams(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Team")
        teams = [Team(team_id, team_name) for team_id,team_name in cur.fetchall()]
        return teams

    @staticmethod
    def createTeam(team_name, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO Team (team_name) VALUES (%s)", (team_name,))
        conn.commit()
        cur.execute("SELECT * FROM Team WHERE team_name = %s", (team_name,))
        [team_id, team_name] = cur.fetchone()
        team = Team(team_id, team_name)
        return team

    @staticmethod
    def deleteTeam(team_id, conn):
        cur = conn.cursor()
        cur.execute("DELETE FROM Team WHERE team_id = %s", (team_id,))
        conn.commit()

    def getMembers(self, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Member WHERE team_id = %s", (self.team_id,))
        members = [Member(user_id, team_id, role) for user_id,team_id,role in cur.fetchall()]
        return members

    def removeMember(self, user_id, conn):
        cur = conn.cursor()
        cur.execute("DELETE FROM Member WHERE user_id = %s AND team_id = %s", (user_id, self.team_id))
        conn.commit()

    def addMember(self, user_id, role, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO Member (user_id, team_id, role) VALUES (%s, %s, %s)", (user_id, self.team_id, role))
        conn.commit()

    def updateTeamName(self, team_name, conn):
        cur = conn.cursor()
        cur.execute("UPDATE Team SET team_name = %s WHERE team_id = %s", (team_name, self.team_id))
        conn.commit()
        self.team_name = team_name

class Member:
    def __init__(self, user_id, team_id, role):
        self.user_id = user_id
        self.team_id = team_id
        self.role = role
    
    @staticmethod
    def getMember(user_id, team_id, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM member WHERE user_id = %s AND team_id = %s", (user_id, team_id))
        [user_id, team_id, role] = cur.fetchone()
        member = Member(user_id, team_id, role)
        return member

    def setRole(self, role, conn):
        cur = conn.cursor()
        cur.execute("UPDATE member SET role = %s WHERE user_id = %s", (role, self.user_id))
        conn.commit()
        self.role = role