class Team:
    def __init__(self, team_id, team_name):
        self.team_id = team_id
        self.team_name = team_name

class Member:
    def __init__(self, user_id, team_id, role):
        self.user_id = user_id
        self.team_id = team_id
        self.role = role