from datetime import datetime
class Bills:
    def __init__(self, name, currency = "£"):
        self.bill_name = name
        self.bill_currency = currency
        self.bill_transactions = []


    def show_bill(self):
        return f"{self.bill_name} - {self.bill_currency}{self.bill_transactions[0]['amount']}"
    
    # def pay_bill(self, amount):
    #     self.bill_amount -= amount

    def add_transaction(self, title="", description="", amount=0,
                         sender="", receiver=""):
        new_transaction={
            "transaction_id" : len(self.bill_transactions)+1,
            "date" : datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            "title" : title,
            "description" : description,
            "amount" : amount,
            "sender" : sender,
            "receiver" : receiver,
        }

        self.bill_transactions.append(new_transaction)
