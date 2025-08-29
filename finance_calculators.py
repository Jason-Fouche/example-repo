import math


# Printing the message for the user to follow
MENU = """ 
Investment - to calculate the amount of interest you'll earn on 
              your investment.
Bond       - to calculate the amount you'll have to pay on a home loan.

Enter either \"investment\" or \"bond\" from the menu above to proceed:
"""
print(MENU)


# Formatting the users responce such that it will always be in lower case and only one of the 2 options provided
response = input().strip().lower()


# Create an If statement for when the user chooses "investment"
if response == "investment":
    print("")
    deposit = input("Enter the amount to deposit : ")
    interest_rate = input("Enter the yearly interest rate(% Excluded) : ")
    interest_rate = interest_rate.replace("%","")               # If the user enters the "%", this line will replace it
    #print(interest_rate)
    years = input("Enter the number of years you plan to invest : ")
    interest = input('Do you want "simple" or "compound" interest? ').strip().lower()

    # Create variables to fit into formulae
    interest_rate = float(interest_rate)/100              # Interest devided by 100
    deposit = float(deposit)                              # Deposit amount
    years = float(years)                                  # Number of years being invested

    # Create a nested if loop to see if the user uses simple or compound interest
    if interest == "simple":
        answer = deposit * (1 + interest_rate * years)           # A = P * (1 + r * t)
        print(f"The final amount: {answer:.2f}")            
    elif interest == "compound":
        answer = deposit * math.pow((1 + interest_rate), years)          # A = P * (1 + r) ** t
        print(f"The final amount: {answer:.2f}")            
    else:
        print("ERROR. Please check your spelling and retry")


# Create an If statement for when the user chooses "bond"
elif response == "bond":
    print("")
    value = input("Enter the present value of the House: ")
    interest_rate = input("Enter the yearly interest rate(% Excluded) : ")
    interest_rate = interest_rate.replace("%","")
    months = input("Enter the number of months you plan to repay the bond: ")


    # Create variables to fit into the formula
    value = float(value)                          # Present value of the house
    interest_rate = (float(interest_rate) / 100) / 12     # Monthly interest rate
    months = float(months)                         # Number of months the bond will be paid

    repayment = (interest_rate * value) / (1 - (1 + interest_rate) ** (-months))              # (i * P) / (1 - (1 + i) ** (-n))
    print(f"The monthly repayment: {repayment:.2f}")            # Format specifier is used


# If the user misspelled either investment or bond, or entered a different word. The user wil be prompted to rerun the code
else:
    print("ERROR. Please check your spelling and retry")
