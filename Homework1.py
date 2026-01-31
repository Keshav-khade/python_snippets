# some question little code snippets

# Q1. WAP that asks the user to enter the width and height of a rectangle and then computes and prints it's area.

def Area_of_a_rectangle(width , height):
    x = width
    y = height
    area = (width * height)
    return area

x = int(input("Enter a width of a rectangle: "))
y = int(input("Enter a height of a rectangle: "))
Total_area=Area_of_a_rectangle(x,y)
print(f"The area of a rectangle is : {Total_area}")

# Q2.  WAP that asks for a number of minutes and convert it into the seconds.

def Minutes_into_second(minutes):
    x = minutes
    seconds = (x * 60)
    return seconds

x = int(input("Enter the number of minutes: "))
seconds = Minutes_into_second(x)
print(f"{x} Minutes = {seconds} seconds")


# Q3. asks for two intergers and print their sum and average

def sum(a , b):
    total_sum = a+b
    return total_sum

def average(a , b):
    """ this function calculates average for just tow number"""
    total_sum = sum(a,b)
    Average =  total_sum / 2
    return Average , total_sum

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

Average , total_sum = average(x,y)
print(f"Your average is:{Average} & Your sum is:{total_sum}")


# Q4. asks for product price and taxes and print total 

def Total_cost(price,percent):
    total_cost = price + Total_tax(price,percent)
    return total_cost

def Total_tax(price,percent):
    total_tax = (price * (percent / 100))
    return total_tax

price =  float(input("Enter the price of a product: "))
percent = float(input("Enter the percent of tax: "))

final_price = Total_cost(price,percent)
print(f"The final price of your product is: {final_price}₹ including: {percent}% tax")
print("Thank you for shopping sir !")
    
    
