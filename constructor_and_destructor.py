"""
# this is how you can construct a user defined constructor for initializing objects
class Student:
    def __init__(self, name, age):
        print("Constructor called!")
        self.name = name
        self.age = age

s1 = Student("Raju", 20)   # yahi line __init__ ko trigger karti hai
s1.display()
"""

"""
# Jab tum Student("Raju", 20) likhte ho, actually do cheezein hoti hain:
# __new__ — yeh actual object ko memory mein banata hai (heap mein khaali jagah allocate karta hai)
# __init__ — yeh us already-bane object ko initialize karta hai (values set karta hai)
# in python there is not concept of method overloading so you can not define two constructors in one class

class Rectangle:
    def __init__(self, length, width=None):
        if width is None:
            width = length     # square banane ke liye
        self.length = length
        self.width = width
        print(f"{self.length}\t{self.width}")

r_square = Rectangle(5)        # square: 5x5
r_rect = Rectangle(5, 3)       # rectangle: 5x3
"""

"""
destructors in python :
1. 
class Student:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def __del__(self):
        print(f"{self.name} destroyed")

s1 = Student("Raju")
del s1        # ya program end ho jaaye, tab bhi call hoga
"""

"""
# class for calculating total and average marks of a student. Demonstrating concept of local variables.
class Student:
    def __init__(self, name):
        self.name = name # instance variable
        self.marks = []

    def get_marks(self, *marks):
        ''' *marks is accepting any number of positional arguments'''
        for m in marks: # m is local here
            self.marks.append(m)

    def average(self):
        total = sum(self.marks) # local variable
        count = len(self.marks)
        return total, total / count

s1 = Student("kartik")
s1.get_marks(10, 20, 30, 40, 50)
Total, avg = s1.average()
print(f"Total is: {Total}\nAverage is: {avg}")
"""

"""
# how to define parameterless constructor

class Demo:
    def __init__(self): # 
        print("object initialized")
        self.roll_no = 0
        self.stud_name = ""

    def get_data(self):
        self.roll_no = 1001
        self.stud_name = "Rajesh"

    def display(self):
        print("from display method")
        print("roll_no= ", self.roll_no)
        print("Name =", self.stud_name


d = Demo()  # instance
d.get_data()
d.display()  # message passing

d.__init__()
# d.__init__()
"""

"""
# how to work with parameterized constructor

class Demo:
    def __init__(self, p1, p2):
        print("object initialized")
        self.p1 = p1
        self.p2 = p2

    def display(self):
        print(f"first parameter: {self.p1}")
        print(f"second parameter: {self.p2}")


a = int(input("Enter first values:"))
b = int(input("Enter first values:"))
# b = int("Enter second values:")

d = Demo(a, b)
d.display()
"""

"""
                                                    Destructor
ex1.
class Student:
    def __init__(self):
        print("object is created")
        self.name = "kartik"
    def __del__(self):
        print("object destroyed")
        print(f"{self.name} destroyed")

s1 = Student()
del s1
print("Thank you")

ex2.
class Student:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print(f"{self.name} destroyed automatically")

s1 = Student("Sita")
print("program ending...")
# yahan koi 'del' nahi likha, phir bhi program end hote hi __del__ call hoga

ex3.
class FileHandler:
    def __init__(self, filename):
        print("Enter into object")
        self.f = open(filename, 'w')

    def __del__(self):
        print("get out into object")
        self.f.close()  # yeh timing guaranteed nahi hai!
        print(f"is file closed successfully {self.f.closed}")
        
f = FileHandler("demo.txt")
print("destructor called successfully")
del f

ex4.
Method	Kab call hota hai
__init__	Jab object banta hai (ClassName())
__del__	Jab object destroy hota hai (ref count 0)
__enter__	Jab with statement shuru hota hai
__exit__	Jab with block khatam hota hai (chahe normally ya error ke saath)


with : 
Python ka ek special statement hai resource management ke liye — file handling, database connection, locks, etc. Yeh guarantee deta hai ki cleanup hamesha hoga, chahe block ke andar error hi kyun na aa jaaye.

open() 
internally __enter__/__exit__ use karta hai. Ab dekho apna khud ka class banake yeh same behavior kaise milta hai.

ex1.
class FileHandler:
    def __enter__(self):
        self.f = open("data.txt", 'w')
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()

with FileHandler() as f:
    f.write("hello")
    
ex.2
# Better — context manager
class FileHandler:
    def __enter__(self):
        self.f = open("data.txt", 'w')
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()  # yeh GUARANTEED chalega, 'with' block khatam hote hi


with FileHandler() as f:
    f.write("hello")
# yahan __exit__ automatically chal jaayega

__exit__ -> block extra three parameters
1. Yeh Python ko batate hain ki agar with block ke andar koi error aayi ho toh uske details:
2. if no such errors are there in with block by default it gets values as None 
exc_type — error ka type (jaise ZeroDivisionError)
exc_val — error ka message
exc_tb — traceback

ex3.
this example shows how after getting an error instead __exit__ called by python automatically
class FileHandler:
    def __enter__(self):
        print("Opening file")
        self.f = open("data.txt", 'w')
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file (guaranteed!)")
        self.f.close()
        if exc_type:
            print(f"An error occurred: {exc_val}")
        return False   # False = error ko suppress mat karo, aage propagate hone do

with FileHandler() as f:
    f.write("hello")
    result = 10 / 0    # ← error yahan aayi
"""

"""
# how objects are created internally

class Demo:
    def __new__(cls, *args, **kwargs):
        print("Step 1: memory allocate ho rahi hai")
        instance = super().__new__(cls)   # object.__new__(Demo) ko call kiya
        print("Step 2: khaali object mila, memory ban gayi:", instance)
        return instance

    def __init__(self, value):
        print("Step 3: ab values set ho rahi hain")
        self.value = value

d = Demo(10) 
"""

"""
Q1: What happens if a class doesn't define __init__, and you try to instantiate it with arguments — e.g., MyClass(5, 10)?

Answer: Python raises a TypeError. When no __init__ is defined, Python uses a default constructor that only accepts self — it doesn't know what to do with extra positional arguments like 5 and 10.

class MyClass:
    pass

obj = MyClass(5, 10)
TypeError: MyClass() takes no arguments

Key point: The default constructor supports zero-argument instantiation only. If you want a class to accept arguments, you must explicitly define __init__ with matching parameters.
"""

"""
Q2: Given the following code, what happens after del s1?

ex.
class Student:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} destroyed")

s1 = Student("Raju")
s2 = s1
del s1

Answer: Only the name s1 is removed. The object itself stays alive in memory, and __del__ does not get called yet — because s2 still holds a reference to the same object.

Explanation: In Python, variable names are just labels pointing to objects in memory (this is called reference counting). s2 = s1 doesn't create a copy of the object — it creates a second label pointing to the same object. del s1 removes one label, but the object survives as long as at least one reference (s2) still points to it.

python
s1 = Student("Raju")
s2 = s1
del s1                  # object still alive — s2 still references it
print("s1 removed, object alive")
del s2                  # NOW reference count hits 0 → __del__ fires
s1 removed, object alive
Raju destroyed

Key point: An object is only destroyed (and __del__ called) when its reference count drops to zero — not when any single variable name is deleted.
"""

"""
Q3: If a child class defines its own __init__ but doesn't call super().__init__(), does the parent class's __init__ still run?

Answer: No. The parent's __init__ does not run automatically. It gets completely overridden by the child's __init__, exactly like any other overridden method in inheritance. Any attributes the parent constructor was supposed to set will be missing.

ex1.
class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor ran")

class Student(Person):
    def __init__(self, roll_no):
        # super().__init__() NOT called
        self.roll_no = roll_no
        print("Student constructor ran")

s = Student(101)
print(s.roll_no)   # 101 — works fine
print(s.name)       # AttributeError!
Student constructor ran
101
AttributeError: 'Student' object has no attribute 'name'

Fix — explicitly call the parent constructor:

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)   # parent's __init__ runs first
        self.roll_no = roll_no

Key point: Python does not automatically chain constructors up the inheritance hierarchy. It's the developer's responsibility to call super().__init__() if the parent's initialization logic is needed.
"""

"""
Q4: __init__ mein error aa jaaye — kya object banega?

class Demo:
    def __init__(self, x):
        print("Constructor started")
        self.value = 10 / x    # error yahan aa sakti hai
        print("Constructor finished")   # yeh line kabhi nahi chalegi agar error aayi

d = Demo(0)
Correction: program hamesha crash nahi hota — sirf tab jab error uncaught ho. Aur object "create hoke crash hota hai" — yeh bhi thoda misleading hai: object memory mein allocate hua tha (__new__ se), lekin kabhi fully initialize nahi hua, aur kisi variable ko assign hi nahi hua — isliye usse "successfully created object" kehna sahi nahi, better kahenge "partially constructed, unreachable object jo turant discard ho gaya."
"""

"""
Q5: __del__ ke andar khud error aa jaaye — program crash hoga?

class Demo:
    def __del__(self):
        print("Destructor running")
        raise ValueError("Something went wrong in destructor!")

d = Demo()
del d
print("Program continues normally")

Correction summary: object destroy hota hai (reference count 0 hote hi memory release hoti hai), program crash nahi hota, bas ek warning print hoti hai console pe aur baaki program normally continue karta hai.
"""

"""
Q6: p1's __del__ chalne se kya p2 affect hota hai?

class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")
    def __del__(self):
        print(f"{self.name} destroyed")

p1 = Person("Raju")
p2 = Person("Sita")

del p1              # ← sirf p1 destroy hoga
print("p2 still exists:", p2.name)   # ✅ p2 bilkul safe hai
del p2

Bilkul sahi samjhe — p1 aur p2 do completely alag objects hain (do alag memory blocks, do alag __dict__), sirf isliye ki dono same class se bane hain, iska matlab yeh nahi ki unka lifecycle judaa hai. Har object apna independent reference count rakhta hai, aur __init__/__del__ har object ke liye alag se, uski apni memory ke basis pe trigger hote hain.
"""