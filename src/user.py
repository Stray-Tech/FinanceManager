from datetime import datetime

users = {}

class User:
    """This is a class for Users.

    Arguments:
        name {string} -- name of the user
        balance {number} -- initial balance from all current accounts
    
    Properties:
        ID {string} -- a constant unique identifier
        name {string} -- name of the user
        balance {number} -- initial balance from all current accounts
    
    Methods:
        get_id {function} -- returns user's ID
    """  
    def __init__(self, name:str, balance:float) -> None:
        self.ID = f"{len(users)+1}_{name}_{datetime.timestamp}"
        self.NAME = name
        self.balance = balance
    
    def get_id(self) -> str:
        return self.ID

def create_user(name:str, balance:int) -> None:
    new_user = User(name, balance)
    users[new_user.get_id()] = new_user

def delete_user(ID:str) -> None:
    del users[ID]

# user class should work with other classes to keep information specific to an individual user.