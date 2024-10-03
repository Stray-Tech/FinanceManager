from datetime import datetime

class Pots:
    def __init__(self, name="new pot", currency="£", amount=0) -> None:
        self.pot_name = name
        self.pot_currency = currency
        self.pot_amount = amount
        self.pot_transactions = []
    
    def deposit(self, amount) -> None:
        self.pot_amount += amount

    def withdraw(self, amount) -> None:
        self.pot_amount -= amount

    def add_transaction(self, title="", description="", amount=0, sender="", receiver=""):
        new_transaction={
            "transaction_id" : len(self.pot_transactions)+1,
            "date" : datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            "title" : title,
            "description" : description,
            "amount" : amount,
            "sender" : sender,
            "receiver" : receiver,
        }

        self.pot_transactions.append(new_transaction)