"""
look up chain order
p1 (reference) 
   → points to the object in heap 
      → object's own __dict__ is checked first (empty here)
      → not found? → Python follows object.__class__ -> print(p1.__class__) → Person's __dict__
      → finds name = "raju", age = 25, talk() there

class Person: # class object in memory
          name = "raju"
          age = 25

          def talk(cls):
                  print("name: ",cls.name)
                  print("age: ",cls.age)

p1 = Person() # address for object in memeory
p1.talk()

print(Person.__dict__)
print(p1.__dict__)
print(p1.__class__)
"""

"""
class Person: # class object in memory
          name = "raju"
          age = 25

          def talk(cls):
                  print("name: ",cls.name)
                  print("age: ",cls.age)
print(Person.name)
print(Person.age)
print(Person.talk(Person)) # you can do this in case of class variables but for instance variable it might throw nameError. this is identical to Person.talk(p1) when you call p1.talk().
"""

"""
class Demo:
          a = 70 #static variables / class variables
          _b = 29
          __c = 82
print(Demo.a)
print(Demo._b)
print(Demo.__c) #private static variable can't access outside of the class. but accessed using name mangling.
print(Demo.__dict__) #this dict variable would be useful for see mangled name for private variables.
"""

'''
class Person:
        name = "kartik"
        age = 25
        def __init__(self,name,age):
                self.name = name
                self.age = age

        @classmethod
        def talk(self):
           print(f"your name: {self.name} and age is: {self.age}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
p1 = Person(name,age) # constructor with parameters
# print(p1.__dict__) 
# Person.talk() # class name can't call instance methods
# p1.talk() # this will worked because python interpret it as Person.talk(p1)
# print(Person.name) # will not work because you can't access instance variable thru class name
# print(Person.__dict__)
'''

"""

class Person:
        name = "kartik"
        age = 25
        def __init__(self):
                self.name = "rohit"

        @classmethod
        def greet(cls):
                '''That's the entire point of the decorator — it changes what gets passed, ignoring whether you called it through an object or the class name'''
                print(f"name: {cls.name}, age= {cls.age}")
p1 = Person()

p1.greet() # Person.greet(p1) because objects share the attributes of class
p1.greet() # Person.greet(Person) in case of classmethod python work like this
Person.greet()
print(Person.__dict__['name']) #method of fetching something from class dictionary
"""

# class sample:
#         a = 27

#         def show(self):
#                 print("from show method of smaple class")
#                 self.i = 14
#         def cal(self):
#                 self.i = self.i + 15
#                 sample.a = sample.a + 30
#         try:
#                 def dis(self):
#                         print("from display method of sample class")
#                         self.i = self.i + 10
#                         print("i= ",self.i,"a= ",self.a)
#         except AttributeError as e:
#                 print("your methods attributes has not defined yet",e)

# # print(sample.__dict__)
# s1 = sample()
# s2 = sample()
# s2.dis()

# class sample:
#     def dis(self):
#         print("from display method")
#         self.helper()          # ← ek aur method ko call kar rahe hain andar se

#     def helper(self):
#         self.i = self.i + 10   # ← actual error yahan hogi

# s2 = sample()
# s2.dis()

"""
Note: 1. exception must be catch in valid places in class you can use them under method or in class body over methods, or in module level
2. Errors returns back from where it is propagate or called.
"""

"""
# program for calculating the area and perimeter of a circle

import math
class Circle:
        def __init__(self):
                self.radius = 0
        def get_data(self):
                self.radius = int(input("Enter radius: "))
        def area(self):
                self.area = math.pi * self.radius ** 2
                return self.area
        def perimeter(self):
                self.perimeter = 2 * math.pi * self.radius
                return self.perimeter
c1 = Circle()
c1.get_data()

print(f"Area of a circle: {c1.area()}")
print(f"perimeter of a circle: {c1.perimeter()}")
"""

"""
# create a class called product and display the total amount and gst amount final payable for customers

class Product:
        def __init__(self):
                self.pro_id = 0
                self.pro_name = ""
                self.pro_price = 0
                self.pro_qty = 0
                self.gst = 0
        def get_data(self):
                self.pro_id = int(input("Enter product id: "))
                self.pro_name = input("Enter product name: ")
                self.pro_price = int(input("Enter product price: "))
                self.pro_qty = int(input("Enter product qty: "))
                self.pro_gst = int(input("Enter product gst (in percentage): "))
        def cal(self):
                self.total = self.pro_price * self.pro_qty
                self.gst_amount = self.total * (self.pro_gst/100)
                self.final_payable = self.total + self.gst_amount
        def display(self):
                print("------------------welcome to our shop------------------")
                print(f"product_id: {self.pro_id}\tproduct_name: {self.pro_name}")
                print(f'Total quantity: {self.pro_qty}\tPrice_per_item: {self.pro_price}')
                print(f"\tTotal_amount: {self.total}\n\tIncluded_gst: {self.gst_amount}")
                print(f"\tfinal_payable: {self.final_payable}")
                print(f"------------------Thank you !--------------------------")

c1 = Product()
c1.get_data()
c1.cal()
c1.display()
"""     

"""
Local variable inside method of a class
1. A variable created inside a method of a class without using self parameter is called local variable.
2. local variables works only within that method.
3. local variable created in one method or you want to use it in another method pass them as a argument to another method
4. once method is over than python removes that variables from memory.
5. use them when you have to use constants in your method like in below example pi.
6. use them only for temporary calculations.

ex1.
class Circle:
    def __init__(self, radius):
        self.radius = radius   # yeh baar baar chahiye → instance attribute

    def area(self):
        pi = 3.14159            # ← sirf isi calculation ke liye chahiye → local
        result = pi * self.radius ** 2   # ← yeh bhi sirf yahi return hoke chala jaayega
        return result

ex2. 
c = Circle(5)
print(c.area())     # 78.53975
print(c.radius)     # ✅ 5 → kyunki self.radius tha
# print(c.pi)       # ❌ error → pi kabhi object mein save hi nahi hua
class Calculator:
    def add(self, a, b):
        result = a + b # local attribute
        self.result = a + b   # ← instance attribute (self ke saath)
        print("Sum:", self.result)
        print("Sum:", result)

c = Calculator()
c.add(5, 3)
print(c.result)   # ✅ works! 8 — kyunki self.result object mein save hua tha
print(c.__dict__)
print(Calculator.__dict__)

"""
