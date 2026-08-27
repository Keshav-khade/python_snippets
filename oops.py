#                   oops in python
# class called student which describes students and decide pass and fail


# "Fail gracefully" — program crash mat karo, gracefully handle karo aur default value ke saath aage badho

# class student:
#           def __init__(self):
#                   try:
#                     self.name = input("Enter your name: ")
#                     self.age = int(input("Enter your age: "))
#                     n = int(input("Enter number of subjects you have: "))
#                     self.marks = []
#                     for i in range(1,n+1):
#                               x = int(input(f"Enter you sub{i} marks: "))
#                               self.marks.append(x)
#                   except Exception as e:
#                           print("Error: ",{e})
                          
                  
#           def display(self):
#                     try:
#                               print(self.name)
#                               print(self.age)
#                               print(self.marks)
#                     except Exception as e:
#                               print("Error: ",{e})
                            
#           def result(self):
#                     try:
#                               sum =0
#                               for x in self.marks:
#                                         sum += x
#                               if sum > 40:
#                                         print("pass")
#                               else:
#                                         print("fail")
#                     except Exception as e:
#                             print("Error: ",{e})

# try:
#           stud1 = student() # student.__new__(student) -> student.__init__(obj) -> stud1 = obj
#           stud1.display() # student.display(stud1)
#           stud1.result() # student.result(stud1)
# except Exception as e:
#         print("Error: ",{e})

# try:
#           stud2 = student()
#           stud2.display()
#           stud2.result()
# except Exception as e:
#         print("Error: ",{e})

'''
          this is an example of abstraction in oops

class Bank:
          def __init__(self):
                  self.acc_no = int(input("Enter your account number: "))
                  self.acc_name = input("Enter your account name: ")
                  self.acc_balance = float(input("Enter your account balance: "))
                  self.__loan = float(input("Enter your loan amount: "))

          def display_to_clerk(self):
                  print(f"your account number is: {self.acc_no}")
                  print(f"your account name is: {self.acc_name}")
                  print(f"your current balance is: {self.acc_balance}")
                  print(f"your current loan amount is: {self.loan}")
cust1= Bank()
cust1.display_to_clerk()
print(cust1.loan)
'''

'''
                    exa. for inheritance
class A:
          a = 1
          b = 2

          def display1(cls):
                  print(cls.a)
                  print(cls.b)
class B(A):
        c = 3

        def display2(cls):
                print(cls.c)

obj = B()
print(obj.a)
print(obj.b)
print(obj.c)
obj.display1()
obj.display2()

'''
