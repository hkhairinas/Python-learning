# income = float(input("Enter the annual income: "))

# if income < 85528 :
#     tax = (18/100)*income-556

# if income > 85528 :
#     inc = (income - 85528) * (32/100)
#     tax = 14839 + inc

# if tax < 0. :
#     tax = 0.
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")

# ------------------------------------------------------------------

year = int(input("Enter a year: "))
if year % 4 != 0: print("Common Year")
elif year % 100 !=0: print("Leap Year")
elif year % 400 !=0: print("Common Year")
else: print("Leap Year")
if year <= 1582: print("Not within the Gregorian calendar period")
