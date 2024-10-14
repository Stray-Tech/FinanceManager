# TODO Import Class Bills to test food shopping expense
from bills import Bills

# TODO take and show bill name
# TODO show total food shopping bills inc name and cost
food_shopping = []
def create_bill():
    index = 0
    while True:
        user_company_name = input("Please can you provide the name for the bill: ")
        user_company_bill_cost = float(input("Please can you provide the cost for this bill: "))
        bill = Bills(name=user_company_name)
        # TODO add user name when combining scripts 
        bill.add_transaction(title=user_company_name,amount=user_company_bill_cost,receiver=user_company_name)
        food_shopping.append(bill)
        should_continue = input("Would you like to add more food shopping bills? Type 'yes or no'.\n").lower()
        if should_continue == "no":
            for x in food_shopping:
                print(f"Your total food shopping bills added = {x.show_bill()}")
            # total_cost = 0
            total_cost = sum([b.bill_transactions[0]['amount'] for b in food_shopping])
            # for bill in food_shopping:
            #     total_cost += bill.bill_transactions[index]['amount']
            print(f"Your total food shopping bills accumulate to: {bill.bill_currency}{total_cost}")
            break         
        elif should_continue == "yes":
            print(f"Your total food shopping bills spent = {food_shopping[index].show_bill()}")
            index += 1
create_bill()


# TODO pay bill showing receiver sender and bill cost
def get_payment_information():
    food_shopping[0].bill_transactions[0]['receiver']
get_payment_information()
# TODO show current balance and balance after paying bill