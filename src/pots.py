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