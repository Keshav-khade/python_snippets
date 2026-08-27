# input radius and calculate and area and perimeter of a circle
#Jo names import kiye hain unhe directly use karo: Isme math.pi ki jagah sirf pi use hoga.
# from math import pi,pow

'''
# area -> pi*r^2 , Perimeter -> 2*pi*r

def cal_area(radius):
          return (pi * pow(radius,2))

def cal_perimeter(radius):
        return (2*pi*radius)

try:
        radius = float(input("Enter a radius for a circle:"))
        area = cal_area(radius)
        perimeter = cal_perimeter(radius)
except Exception as e:
        print(e)
else:
        print("area of a circle: ",area)
        print("perimeter of a circle: ",perimeter)
'''

'''
def area(side):
        return side*side
def perimeter(side):
        return 4*side
try:
        side = int(input("Enter side of a square: "))
        area_sqr = area(side)
        perimeter_sqr = perimeter(side)
except Exception as e:
        print(e)
else:
        print(f"area is: {area_sqr} \n perimeter is: {perimeter_sqr}")
'''

'''

def acceleration(mass,force):
        accelerate = force / mass
        return accelerate

try:
        mass = float(input("Enter the mass of a object: "))
        force = float(input("Enter the force applied on a object: "))
        result = acceleration(mass,force)
except Exception as e:
        print(e)
else:
        print(f"the value of acceleration is: {result}")

'''


'''
def area_triangle(length,width):
        area = (1/2*length*width)
        return area

try:
        length = int(input("given length: "))
        breadth = int(input("given breadth: "))
        result = area_triangle(length,breadth)
except Exception as e: 
        print("read your error: ",e)

else:
        print(f"the are of triangle is: {result}")
'''

'''
def perimeter_triangle(side1,side2,side3):
        return side1 + side2 + side3

try : 
        side1,side2,side3 = [int(x) for x in input("Enter three value: ").split(",")]
        perimeter = perimeter_triangle(side1,side2,side3)
except Exception as e:
        print(e)
else:
        print(f"Perimeter of a triangle is: {perimeter}")
'''


'''
def cal_area(len,wid):
        return len*wid

def cal_perimeter(length,width):
        return 2*(length+width)

try:    
        length = float(input("Enter the length of rectangle: "))
        width = float(input("Enter the width of rectangle: "))
        area = cal_area(length,width)
        perimeter = cal_perimeter(length,width)
except Exception as e:
        print(e)
else:
        print(f"area of a rectangle is: {area} \n perimeter of a rectangle: {perimeter}")
'''


'''
def cal_gst(total,rate):
        gst = total * (rate/100)
        return gst

def sub_bill(qty,price):
        return (qty*price)

def Net_bill(total,gst):
        return total + gst

try:
        pcode = int(input("Enter your id: "))
        pname = input("Enter your name: ")
        qty = int(input("Enter total quantity: "))
        price = float(input("Enter per item cost: "))
        gst_rate = float(input("Enter your rate: "))

        total = sub_bill(qty,price)
        gst = cal_gst(total,gst_rate)
        final_amount = Net_bill(total,gst)

except Exception as e:
        print(e)

else:
        print("your receipt: ")
        print(f"\t your code: {pcode}")
        print(f"\t your name: {pname}")
        print(f"\t your gst: {gst}")
        print(f"\t your final payable: {final_amount}")
        print("Thank you for shopping sir !")
          
'''

'''
def total_marks(lst):
        sum = 0
        for x in lst:
                sum += x
        return sum

def average(len,sum):
        avg = sum / len
        return avg

try:
        stud_id = input("Enter your student id: ")
        stud_name = input("Enter your name: ")
        n = int(input("How many subjects you have: "))
        lst = []
        for i in range(1,n+1):
                marks = int(input(f"Enter your marks in sub{i}: "))
                lst.append(marks)
        num_of_sub = len(lst)
        sum = total_marks(lst)
        avg = average(num_of_sub,sum)
except Exception as e:
        print(e)
else:
        print(f"your total marks is: {sum} \n your average is: {avg}")
'''

'''
def convert_to_fahrenheit(celsius):
        fah = ((9/5) * celsius) + 32
        return fah

def convert_to_celsius(fahrenheit):
        cel = (5/9)*(fahrenheit - 32)
        return cel

try:
        cel = int(input("Enter the temperature(in celsius): "))
        fah = int(input("Enter the temperature(in fahrenheit): "))
        celsius = convert_to_celsius(fah)
        fahrenheit = convert_to_fahrenheit(cel)
except Exception as e:
        print(e)
else:
        print(f"\t {cel}: celsius into fahrenheit: {fahrenheit}")
        print(f"\t {fah}: fahrenheit into celsius: {celsius}")
'''