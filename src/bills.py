from datetime import datetime
class Bills:
    def __init__(self, name, currency, amount):
        self.bill_name = name
        self.bill_currency = currency
        self.bill_amount = amount
        self.pot_transactions = []


    def pay_bill(self, amount):
        self.bill_amount += amount

    def add_transaction(self, title="", description="", amount=0,
                         sender="", receiver=""):
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
