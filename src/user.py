users = []

class User:
    def __init__(self, name, balance) -> None:
        self.NAME = name
        self.balance = balance

def create_user(name, balance):
    users.append(User(name, balance))
