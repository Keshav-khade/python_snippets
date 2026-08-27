# type of methods in python under classes
# import math
import sys
'''
type of methods :   1.instance method :
                                        1. accessor method
                                        2. mutator method
                    2. class method :
                    3. static method :
'''

'''
class student:
          # this is a constructor
          def __init__(self,name="",marks=0):
                  self.name = name
                  self.marks = marks

          def display(self):
                  print(f"your name is: {self.name}")
                  print(f"your marks is: {self.marks}")

          def calculate_grade(self):
                    if(self.marks >= 600):
                              print("hey congrats you got first position !")
                    elif(self.marks>=450):
                              print("hey congrats you got second position !")
                    elif(self.marks >= 350):
                              print("hey congrats you got third position !")
                    else:
                              print("sorry you are failed try again !")

# how to create lots of instances
i=0
n= int(input("Enter how many student is a classroom: "))
while(i<n):
          name = input("Enter student name: ")
          marks = int(input("Enter total marks: "))
          print("_____________________________________")
          s = student(name,marks)
          s.display()
          s.calculate_grade()
          i += 1
          print("_____________________________________")
'''

'''
#                                                 accessor and mutator methods
class student:
#           def __init__(self,name,marks):
#                   self.name = name
#                   self.marks = marks

          # setter method for name
          def set_name(self,name):
                  self.name = name

          # getter method for name
          def get_name(self):
                  return self.name

          # setter for marks
          def set_marks(self,marks):
                  self.marks = marks

          # getter for marks
          def get_marks(self):
                  return self.marks
n = int(input("Enter number of students: "))
for i in range(1,n+1):
          name = input("Enter your name: ")
          marks = int(input("Enter your marks: "))
          print("________________________________")
          s = student()
          s.set_name(name)
          s.set_marks(marks)
          n_res = s.get_name()
          m_res = s.get_marks()                  
          print("your name is "+n_res)
          print("your name is "+str(m_res))
'''

'''
class methods: without any object we can access class members when every object or calculation needed same method or variable so why we need to create objects

class Bird:
        wings = 2

        @classmethod
        def fly(cls,name):
                print(f"{name} flies with {cls.wings} wings")

# b1 = Bird()
Bird.fly("sparrow")
Bird.fly("pigeon")
'''


'''
static method : just normal function but related to class calculation so put inside the class using @staticmethod
it's independent to any classes or objects has it's own parameter and performs some calculation


class Myclass:
        obj_count = 0

        # constructor
        def __init__(self):
                Myclass.obj_count += 1

        # normal instance method
        def no_object_v1(self):
                print(f"no of objects are: {self.obj_count}")

        # classmethod
        @classmethod
        def no_object_v2(cls):
                print(f"no of objects are: {cls.obj_count}")

        # static method
        @staticmethod
        def no_objects_v3():
                print(f"number of objects created is: {Myclass.obj_count}")

# here you created a object
obj = Myclass()

#for instance method
obj.no_object_v1() # Myclass.no_object_v1(obj)

# for class method
Myclass.no_object_v2() # Myclass.no_boject_v2(myclass)

# for static method
Myclass.no_objects_v3()

'''
'''
how static method used in validation in real systems
password validation, credential validation, 

class student:
          # setter method for name
          def set_name(self,name):
                  self.name = name

          # getter method for name
          def get_name(self):
                  return self.name

          # setter for marks
          def set_marks(self,marks):
                  self.marks = marks

          # getter for marks
          def get_marks(self):
                  return self.marks

          # normal function outside the class you just organize it with class for validation
          @staticmethod
          def validate(marks):
                if 5 <= marks <= 100:
                        print("your marks are in valid range !")
                        return True
                else:
                        return False

                  
n = int(input("Enter number of students: "))
for i in range(1,n+1):
                while True:
                        name = input("Enter your name: ")
                        marks = int(input("Enter your marks: "))
                        res = student.validate(marks)
                        if res:
                                break
                        else:
                                print("please give valid marks and try again")
                             
                s = student()
                s.set_name(name)
                s.set_marks(marks)
                n_res = s.get_name()
                m_res = s.get_marks()                  
                print("your name is "+n_res)
                print("your marks is "+str(m_res))
'''

'''
class sample:
        @staticmethod
        def calculate(x):
                return math.sqrt(x)
  

res = sample.calculate(5)
print(f"value is: {res}")
'''

'''
class Bank:
        # constructor
        def __init__(self,name,balance=0):
                self.name = name
                self.balance = balance
                print("your account is opened successfully !")
        
        # for deposit some amount
        def deposit(self,amount):
                self.balance += amount
                return self.balance

        # for withdraw some amount
        def withdraw(self,amount):
                if amount > self.balance:
                        print("money if not sufficient to withdraw !")
                        print(f"your current balance is: {self.balance}")
                else:
                        self.balance -= amount
                        return self.balance

        # for checking old balance 
        def get_balance(self):
                return self.balance


# object of a bank class
name = input("Enter your name: ")
b = Bank(name)

while True:
        print("d - deposit() | w - withdraw() | e - exit()")
        choice = input("Enter your need:(Example : d | w | e): ")
        if choice == "e" or choice == "E":
                sys.exit()
        amount = float(input("Enter your amount: "))
        if choice =="d" or choice=="D":
                print(f"your old balance is: {b.get_balance()}")
                print(f"your updated balance is: {b.deposit(amount)}")
        elif choice == "w" or choice== "W":
                print(f"your old balance is: {b.get_balance()}")
                print(f"your current balance after withdraw: {b.withdraw(amount)}")
'''
