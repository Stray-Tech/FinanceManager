
def personalBills():
    personal_bills_dict = {

    }
    currency_format = input("Please provide what currency you get paid in '$', '£', '€'" ).lower()
    continue_adding_bills = True
    while continue_adding_bills:
        pb_name = input("Please provide the name for your personal bill ")
        pb_cost = float(input("Please provide the cost for your personal bill "))
        personal_bills_dict[pb_name] = pb_cost
        should_continue = input("Would you like to add more personal bills? Type 'yes or no'.\n").lower()
        if should_continue == "no":
            continue_adding_bills = False
            print("Personal bills & Cost:")
            for key, value in personal_bills_dict.items():
                print(f"{key}: {currency_format}{value}")
            total_cost = sum(personal_bills_dict.values())
            print(f"Your total personal bills spent = {currency_format}{total_cost}")
        elif should_continue == "yes":
            print("\n" * 0)

personalBills()
