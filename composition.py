"""
composition terminologies :
1. outer class object
2. inner class object

when there is no chance to create contained object without a container object, which means contained and container objects are strongly associated and it is called composition

in composition there is a has-a relationship, like car has a engine without car there is no sense of making engine

-> has-a -> car has-a engine
-> part-of -> sterio is part-of car
-> part-of -> salary part-of Employee
-> owns-a -> car owns-a engine
-> owns-a -> Employee owns-a salary

one object owns another object

if container object is destroyed then automatically contained object also gets destroyed

to delete the object of container class -> use del keyword

it is strongly dependent on each other
"""

"""
# ex.1
class Engine:
    def start(self):
        print("Engine starts")
class Car:
    def __init__(self):
        print("object created")
        self.obj = Engine()

    def start_car(self):
        self.obj.start()
        print("car moving")

car = Car()
car.start_car()

"""

"""
ex.2
class Battery:
    def charge(self):
        print("Battery charging")

class Phone:
    def __init__(self):
        print("phone created")
        self.battery = Battery()

    def turn_on(self):
        print("turn on the phone")
        self.battery.charge()

p = Phone()
p.turn_on()

"""

"""
Example 3 :

class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

Here:
A Car has an Engine.
Car contains an object of the Engine class.
"""

"""
why we need composition :
1. Better code handling or organization
every class handles its own resposibilities

2. more flexible design
instead of putting everything inside one class we use every class method and attributes separately

3.Every Object Has Its Own Identity, it prevents accidental modification between shared objects
class Engine:
    pass
class Car:
    def __init__(self):
        self.engine = Engine()
car1 = Car()
car2 = Car()

4. in composition two scenarios are possible -> Creating New Object vs Sharing Object
car1 = Car()
car2 = Car() -> with every different object there is a different contained object

engine = Engine()
car1.engine = engine
car2.engine = engine -> using existed object can lead to data leak

Object Mutation Through Shared References are also possible 

5. == vs is in Python
== -> __eq__ special method which compares objects as well as their data
is -> compares identity or reference of two objects when we compare two objects with each other

6. __eq__ ->  __eq__() Magic Method / __eq__() defines how objects should be compared.
Example:
class Student:
    def __init__(self,name):
        self.name = name
    def __eq__(self,other):
        return self.name == other.name
s1 = Student("John")
s2 = Student("John")
print(s1 == s2)

7. Default Equality Behavior / Without __eq__():
by default it compares object ideantities.

8. questions
Q1. What relationship does composition represent?
Q2. Difference between composition and inheritance?
Q3. What happens when we write:
s2 = s1
Q4. Difference between is and ==?
Q5. What does __eq__() do?

"""

"""
composition example:

class Transaction:
    def __init__(self, bnk):
        print("transaction object created")
        self.bnk_ref = bnk

    def deposit(self, amount):
        self.bnk_ref.acc_balance += amount # how to access the attributes with instance reference
        print(f"your deposited amount is: {amount}\ncurrent balance is: {self.bnk_ref.acc_balance}")
        self.bnk_ref.start_with(amount) # how to access the method

    def withdraw(self, amount):
        self.bnk_ref.acc_balance -= amount
        print(f"your withdraw amount is: {amount}\ncurrent balance is: {self.bnk_ref.acc_balance}")

class Bank:
    def __init__(self,acc_no, acc_name, balance):
        print("Bank object created")
        self.acc_no = acc_no
        self.acc_name = acc_name
        self.acc_balance = balance
        self.transaction = Transaction(self)

    def start_dept(self, amount):
        print("deposit stated")
        self.transaction.deposit(amount)

    def start_with(self, amount):
        print("withdraw started")
        self.transaction.withdraw(amount)

balance = int(input("Enter your account balance: "))
acc_no = int(input("acc nu."))
acc_name = input("acc name.")

b = Bank(acc_no, acc_name, balance)

amount = int(input("amount to be....: "))
b.start_dept(amount)

"""

"""
ex.2 you can access transaction class object only thru bank class object.
class Transaction:
    def __init__(self, bank_ref):
        self.dept_amount = 0
        self.bank_ref = bank_ref   # kis bank account ka transaction hai

    def deposit(self, amount):
        self.dept_amount = amount
        self.bank_ref.acc_balance += amount
        print(f"Deposited. Current balance: {self.bank_ref.acc_balance}")


class Bank:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.acc_name = name
        self.acc_balance = balance
        self.transaction = Transaction(self)   # ✅ COMPOSITION — Bank khud Transaction banata hai
                                                  # apne __init__ ke andar, koi bahar se nahi de raha

b = Bank(101, "Raju", 5000)
b.transaction.deposit(1000)   # transaction object sirf Bank ke through hi accessible hai
"""

"""
Interview Answer ⭐

If an interviewer asks:

"Why use composition instead of nested classes?"

Answer:

"Nested classes organize classes that are tightly coupled and only have meaning inside another class. Composition is about object relationships and allows independent, reusable objects. Composition provides better flexibility because the contained object can be replaced or reused by different classes."

ex.1 nested classes low resulability and flexibility
class Car:
    class Engine:
        def start(self):
            print("Engine started")

    def __init__(self):
        self.engine = Car.Engine()

car = Car()
car.engine.start()

ex.2  composition independent structures and can reuse by other objects and classes also
class Engine:
    def start(self):
        print("Engine started")
        
class Car:
    def __init__(self):
        self.engine = Engine()

car = Car()
car.engine.start()
"""

