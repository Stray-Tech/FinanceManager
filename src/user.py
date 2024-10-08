from datetime import datetime

users = {}

class User:
    def __init__(self, name, balance) -> None:
        self.ID = f"{len(users)+1}_{name}_{datetime.timestamp}"
        self.NAME = name
        self.balance = balance
    
    def get_id(self):
        return self.ID

def create_user(name, balance):
    new_user = User(name, balance)
    users[new_user.get_id()] = new_user

def delete_user(ID):
    del users[ID]