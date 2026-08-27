# how to pass a members of one class to another class
# by passing object of one class to the other class

'''
note: this is called a has-a relationship, here one class utilizes the members of another class without inherit that class
Car "has-a" Engine
Student "has-a" Address
Order "has-a" Customer
employee "has-a" detail

class Emp:
          # initialize
          def __init__(self,id,name,salary):
                  self.id = id
                  self.name = name
                  self.salary = salary

          def display(self):
                  print(f"Employee id: {self.id}")
                  print(f"Employee name: {self.name}")
                  print(f"Employee salary: {self.salary}")

class myclass:

        # static method for changing the attributes
        @staticmethod
        def mymethod(e,amount):
                e.salary += amount
                e.display()

e = Emp('0808ds231064',"kartik",3000)
amt = float(input("Enter your amount: "))
myclass.mymethod(e,amt)

'''

'''
note: when passing objects make sure one can not change the members of other 

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def show_power(self):
        print(f"Engine has {self.horsepower} HP")


class Car:
    def __init__(self, name, engine_obj):   # 👈 dusri class ka object le rahe hain
        self.name = name
        self.engine = engine_obj             # 👈 store kar liya

    def display(self):
        print(f"Car: {self.name}")
        self.engine.show_power()             # 👈 dusre class ka method call kiya!


e1 = Engine(300)         # Engine object banaya

c1 = Car("Mustang", e1)
c2 = Car("BMW", e1)        # 👈 same engine object dono cars ko diya!

c1.display()
c2.display()

e1.horsepower = 500        # Engine directly change kiya

c1.display()
c2.display()
'''