def salaryInput():
    currency_format = input("Please provide what currency you get paid in e.g. '$', '£'").lower()
    user_salary_input = int(input("Please input your full annual salary ").replace(",", ""))
    user_final_salary = '{:,.2f}'.format(user_salary_input)
    print(f"Your annual salary is {currency_format}{user_final_salary}")

salaryInput()