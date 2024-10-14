# TODO Import Class Bills to test food shopping expense
from bills import Bills

# TODO take and show bill name
# TODO show total food shopping bills inc name and cost
food_shopping = []
def create_bill():
    continue_adding_bills = True
    index = 0
    while continue_adding_bills:
        user_company_name = input("Please can you provide the name for the bill: ")
        user_company_bill_cost = float(input("Please can you provide the cost for this bill: "))
        food_shopping.append(Bills(name=user_company_name, amount=user_company_bill_cost))
        should_continue = input("Would you like to add more food shopping bills? Type 'yes or no'.\n").lower()
        if should_continue == "no":
                continue_adding_bills = False
                for x in food_shopping:
                    print(f"Your total personal bills added = {x.show_bill()}")
                total_cost = 0
                for bill in food_shopping:
                    total_cost += bill.bill_amount
                print(f"Your total food shopping bills accumulate to: {food_shopping[0].bill_currency}{total_cost}")         
        elif should_continue == "yes":
            print(f"Your total personal bills spent = {food_shopping[index].show_bill()}")
            index += 1
create_bill()


# TODO pay bill showing receiver sender and bill cost
def get_payment_information():
    pass
# TODO show current balance and balance after paying bill