#                   inner class concept

"""
note : when an existence of a class is matters only to its parent class and that class standalone globally accessible by everyone that time we have to use inner class concept


class Person:
          def __init__(self,dd,mm,yy):
                  self.name = "kartik"
                  self.db = Person.Dob(dd,mm,yy)

          def display(self):
                  print(f"name is: {self.name}")

          class Dob:
                    def __init__(self,dd,mm,yy):
                          self.dd = dd
                          self.mm = mm
                          self.yy = yy

                    def display(self):
                            print("this is your DOB :{}/{}/{}".format(self.dd,self.mm,self.yy))

p = Person(23, 10, 2005)
p.display()
# print(Person.__dict__)
# print(p.__dict__)
# print(p.name)

# address of inner class object stored in outer class constructor
x = p.db

# this x is address of inner class instance
x.display()

print(x.dd)
print(x.mm)
print(x.yy)

"""


'''


class Person:
    def __init__(self, name):
        self.name = name
        self.db = Person.Dob(23,10,2006)

    def display(self):
        print(f"your name is: {self.name}")

    class Dob:
        def __init__(self, dd, mm, yy):
            self.dd = dd
            self.mm = mm
            self.yy = yy

        def display(self):
            print("this is your DOB :{}/{}/{}".format(self.dd, self.mm, self.yy))


p = Person("ram")
p.display()

# direct access of inner class object this is vulnerable practice in oops
db = Person.Dob(23, 10, 2005)

# manipulate the data from outside
db.dd = 25

db.display()
'''

'''
class Person:
    def __init__(self):
        """this is just a constructor"""
        self.name = "kartik"
        self.db = Person.Dob()

    def display(self):
        print(f"name of a person is: {self.name}")

    class Dob:
        def __init__(self):
            """this is also a constructor"""
            self.dd = 23
            self.mm = 10
            self.yy = 2005

        def display(self):
            print("this is your DOB :{}/{}/{}".format(self.dd, self.mm, self.yy))


p = Person()  # person.__new__(Person) -> person.__init__(p)

# // give you the class namespace
print(Person.__dict__)

# __dir__ () or dir() -> gives us the directory means what are the methods and special variables you can use with this class/object
print(dir(Person))

# __init__() -> constructor that's lets you initialize the variables

# __new__() -> construct an empty object inside heap and returns the reference

# __module__ -> tells you in which file/namespace this class defines in return main usually
print(Person.__module__)

# __qualname__ -> gives you the dotted path of the class qualified name
print(Person.Dob.__qualname__)

# __doc__ -> gives you the all docstring or comments written inside the class of method by you but just one docstring
print(Person.__init__.__doc__)

'''

'''
nested classes : 
                        class outer:
                                class inner:
benefits of having :

        1. avoid naming conflicts , keeps then namespace clean
        2. allows you to group the classes that are closely related
        3. allows you to Encapsulate private details that are not useful outside the outer class

'''

'''
# how to avoid naming conflict

class Employee:
        print("this is a Employee class 1")

class Employee:
        print("this is a Employee class 2")

Python doesn't throw an error or warning when you redefine a class with the same name. It just rebinds the name Employee in that namespace to the second class. The first one is gone — garbage collected (assuming nothing else references it).


1. give them different names, otherwise classes can override and class which defined at last only executes.
# file: hr/employee.py
class Employee:
    def __init__(self):
        print("constructor executed")
    pass

# file: finance/employee.py
class Employee:
    def __init__(self):
        print("constructor executed")
    pass
    
from hr.employee import Employee as HrEmployee
from finance.employee import Employee as FinanceEmployee

3. Nest them inside different outer classes
class HR:
    class Employee:
        pass

class Finance:
    class Employee:
        pass
        
print(HR.__dict__)
print()
print(Finance.__dict__)
'''

'''
class Company:
        class Employee:
                def __init__(self,name,position):
                        self.name = name
                        self.position = position

                def get_details(self):
                        return f"Employee Name: {self.name}\nEmployee position: {self.position}"
        

        def __init__(self,company_name):
                self.company_name = company_name
                self.employee  = []

        def add_employee(self,name,position):
                employee_obj = self.Employee(name,position)
                self.employee.append(employee_obj)

        def HR(self):
                return [employee.get_details() for employee in self.employee]

company1 = Company("stark industries")
company1.add_employee("tony stark","CEO")
company1.add_employee("pepper potts","CTO")
company1.add_employee("kartik Khade","software designer")

company2 = Company("wayne enterprises")
company2.add_employee("bruce wayne","CEO")
company2.add_employee("alfred pennyworth","butler")

for employee in company2.HR():
        print(employee)
'''

"""
---------------- this class perfectly shows the concept of object composition --------------------------
class Company:
    class Employee:
        def __init__(self, name, position):
            self.emp_name = name
            self.emp_pos = position

        def get_data(self):
            return f"name : {self.emp_name}\tposition : {self.emp_pos}\n"

    def __init__(self, company):
        self.company = company
        self.employee_lst = []

    def set_emp(self,name,position):
        # local variable for holding the created object
        employee_obj = Company.Employee(name,position)
        self.employee_lst.append(employee_obj)

    def hr(self):
        emp_detail = f"company: {self.company}\n"
        for obj in self.employee_lst:
             emp_detail += obj.get_data()
        return emp_detail

all_companies = []
while True:
    choice = input("Enter your choice to continue further(Y/N): ")
    if choice in "Yy":

        com_name = input("Enter your company name: ")
        # company class
        c = Company(com_name)

        # add employees for this company
        try:
            n = int(input("Enter number of Employee: "))
        except ValueError as e:
            print("Enter valid data Error:\n",e)
            n = int(input("Enter number of Employee: "))

        for i in range(n):
            print(f"-----Employee: {i+1}--------")
            emp_name = input("Enter employee name: ")
            emp_pos = input("Enter employee position: ")

            # set employees
            c.set_emp(emp_name, emp_pos)

        all_companies.append(c)
    else:
        break


print("---------- employee details -------------")
for com_obj in all_companies:
    print(com_obj.hr())
    
    
all_companies (list)
    └── Company object (TCS)
            └── employee_lst (list)
                    ├── Employee object (Raju)
                    └── Employee object (Sita)
    └── Company object (Infosys)
            └── employee_lst (list)
                    └── Employee object (Kartik)
"""

"""
"""
class Bank:
    def __init__(self):
        self.acc_no = 0
        self.acc_name = ''
        self.acc_balance = 0

    def set_data(self):
        self.acc_no = int(input("enter acc nu.: "))
        self.acc_name = input("acc name: ")
        self.acc_balance = int(input("Enter amount: "))

    class Transaction:
        def __init__(self):
            self.dept_amount = 0

        def get_data(self,bnk):
            self.dept_amount = int(input("enter amount to be deposite.: "))
            bnk.acc_balance += self.dept_amount
            print(f"your current amount is: {bnk.acc_balance}")



# bank class
b = Bank()
b.set_data()

# object of transaction class
t = Bank.Transaction()
t.get_data(b)