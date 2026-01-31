										# conditional statements in python #

									# Login validation code using simple if else

User_name = input("Enter your full name: ")
Password = input("Enter your password: ")

if User_name == "admin" and Password == "123":
    print("Login successful")
else:
    print("Login Invalid")


									# Electricity bill amount

units = int(input("Enter total units of this month: "))
if units <= 100:
    "Here we take 9 rupee for per unit"
    bill = units*9
elif units <= 200:
    "Here we take 7 rupee for per unit"
    bill = 100*5 + (units - 100)*7
else:
    "Here we take 10 rupee for per unit"
    bill = 100*5 + 100*7 + (units - 200)*10
print(f"your total amount of this month is Rs {bill}")


									# Discount based on your shoping amount
amount = float(input("Enter your Total amount: "))
if amount >= 5000:
    Discount = amount * .20
elif amount <= 3000:
    Discount = amount * .10
else:
    print("Sorry sir ! you have to buy more items for discount")
print(f"your distcount is: {Discount}")
print(f"your total bill is: {amount - Discount}")