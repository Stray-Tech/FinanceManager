# TODO Import Class Bills to test food shopping expense

from bills import Bills

# TODO take and show bill name
food_shopping = []
def create_bill():
     user_company_name = input("Please can you provide the name for the bill ")
     user_company_bill_cost = input("Please can you provide the cost for this bill ")
     food_shopping.append(Bills(name=user_company_name, amount=user_company_bill_cost))
     print(food_shopping[0].show_bill())

create_bill()


# TODO pay bill showing receiver sender and bill cost
# TODO show current balance and balance after paying bill
# TODO show total food shopping bills inc name and cost