#not imported math as not needed 
investment = str("to calculate the amount of interest you'll earn on your investment")
bond = str("to calculate the amount you'll have to pay on home loan")
print (f"investment - {investment}" '\n' f"bond       - {bond}" '\n''\n' "Enter either 'investment' or 'bond' to proceed: ")

#bond repayment calculation
investment_or_bond_input =input("enter a selection: ").lower().strip() #converts everything to lower case and strip() will remove the spaces after the code
if investment_or_bond_input == "bond":
    house_value =int(input("present value of the house: "))
    interest_rate_bond =int(input("enter the interest rate without %: "))
    repayment_duration =int(input("enter the number of months you plan to take to repay the bond: "))
    bond_repayment =(((interest_rate_bond/100)/12)*house_value)/(1-(1+((interest_rate_bond/100)/12))**(-repayment_duration))
    to_print_b =f"your repayment is {bond_repayment} per month"
    print(to_print_b)

#return on investment calculation 
elif investment_or_bond_input == "investment":
    amount_of_money_depositing =int(input("how much money are your depositing: ").strip()) #refer to comment on line 7
    Interest_rate_entry =int(input("enter the interest rate without %: "))
    duration_invest =int(input("enter the number of years that the money is being invested: "))
    interest =str(input("do you want simple or compound interest? "))
    if interest == "simple":
        interest_applied_simple =amount_of_money_depositing*(1+((Interest_rate_entry/100)*duration_invest))
        to_print_s =f"the amount of interest earned is {interest_applied_simple}"
        print(to_print_s)
    if interest == "compound":
        interest_applied_compound =amount_of_money_depositing* ((1+(Interest_rate_entry/100))**duration_invest) #i decided to use ** instead of math.pow as it is simpler for me, also moved this line below 26 as oppose to above it to ensure the variable existed
        to_print_c= f"the amount of interest earned is {interest_applied_compound}"
        print(to_print_c)
else: 
    print ("Error, please try again")













