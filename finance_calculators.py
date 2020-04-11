#Library for some maths functions.
import math

print("Choose either 'investment' or 'bond' from below to proceed: \n")

print("Investment: To calculate the amount of interest you'll earn on interest\n\n Bond: To calculate the amount you'll earn have to pay on a home loan \n\n")

calculationType = str(input("TYPE IN 'Investment' OR 'Bond' TO MAKE YOUR SELECTION!\n"))

#Line 10-30: Requests and calculates user's investment details.
if(calculationType == "Investment" or calculationType == "INVESTMENT" or calculationType == "investment"):
        deposit = float(input("How much are you depositing?\n"))
        interest_rate = float(input("Key in interest rate.\n"))
        interest_rate_percentage = interest_rate / 100
        investmentPeriod = float(input("How many years are you investing for ?\n"))
        interestType = input("Simple or Compound \nKey in '1' for [Compound Interest] or press enter for [Simple interest]\n")

        if(interestType == 1):
                #Compound interest investment formula.
                Accumulated_amount = deposit * math.pow( 1 + (interest_rate_percentage) , investmentPeriod )    
        else:
                #Simple interest investment formula.
                Accumulated_amount = deposit * ( 1 + (interest_rate_percentage) * investmentPeriod )

                
                #Rounds off final investment accumulated amount to 2 decimal places.
                Accumulated_amount = round( Accumulated_amount , 2)

        #Displays final investment amount.
        print(f"The total accumulated amount you at the end of your investment is R{Accumulated_amount}")       

#Line 33-46: Requests and calculates user's bond details.
elif(calculationType == "Bond" or calculationType == "BOND" or calculationType == "bond"):
	HouseValue = float(input("What is the current value of the house?"))
	interest_rate = float(input("Key in interest rate."))
	interest_rate_percentage = interest_rate / 12
	investmentPeriod = float(input("How many months will you be paying the for ?"))

        #Bond repayment formula
	repayment = HouseValue * ((interest_rate_percentage * math.pow((1 + interest_rate_percentage) , investmentPeriod )) / (math.pow((1 + interest_rate_percentage) , investmentPeriod ) - 1 ))
        #Rounds off final bond repayment to 2 decimal places.
	repayment = round( repayment , 2)

        #Displays final repayment amount.
	print(f"The monthly repayment of the bond is {repayment} ")
        
else:
        print("Invalid Selection. Please try again!")
