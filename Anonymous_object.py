"""
1. Anonymous object or instance is nameless instance created in python.
2. memory creation and working of instance initialization same as named instance.
3. once the class through anonymous instance completes it's execution then it immediately left for the garbage collection

ex.1
class Demo:
    def __init__(self):
        print("enter in constructor")
        self.name = "Keshav"
    def show(self):
        print("from show",self.name)

d1 = Demo()
d1.show()

Demo()

ex.2 how to call an instance method thru anonymous object by calling that method from constructor
class Demo:
    def __init__(self):
        print("from parameterless constructor")
        self.a = 100
        self.show()
    def show(self):
        print("from show", self.a)
Demo()

ex.3

# calling other methods from anonymous object
class Demo:
    def __init__(self):
        self.a = "Keshav"
    def show(self):
        print("from show",self.a)

Demo().show() # method chaining, In this first constructor will be execute then our show() method will
method chaining only works for one method of a class for calling more method by anonymous object you can not use method chaining

ex.4
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

Person("Raju").greet()   # ← koi variable nahi (p1 = ... nahi likha)

ex.5 how anonymous objects are deleted by pythons garbage collector
class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def greet(self):
        print(f"Hello, {self.name}!")

    def __del__(self):
        print(f"{self.name} destroyed")

print("Before anonymous object")
Person("Raju").greet()
print("After anonymous object")

why it is useful:
1. memory management for unnecessary objects
2.Chaining internally kaam karti hai kyunki har method (add) apna khud ka reference (self) return karta hai, jisse agla .method() call usi object pe ho jaata hai — jab tak koi method different cheez return na kare (jaise build() ne string return ki), tab tak chain "same object" pe hi ghoomti rehti hai.


Yeh kaam kyun karta hai — key insight

return self method chaining ko possible banata hai. Har .show() call apna hi object wapas de raha hai, isliye tum usi object pe lagatar methods call kar sakte ho, bina kisi variable mein store kiye:

ex.6

class Demo:
    def __init__(self, x):
        self.x = x
    def show(self):
        print(self.x)
        return self
Demo(5).show().show()


ex.7
Q2: Person('Raju').name

class Person:
    def __init__(self, name):
        self.name = name

Person('Raju').name # standalone method there is no catch for fetched name so nothing will print
"""

"""
# wap to count number of instance created to a class ?
1. create a static variable in a class
2. increment that static variable from constructor
3. print that variable using class name.

ex.1
class Student:
    count = 0
    def __init__(self):
        print("enter into constructor")
        Student.count += 1
s1 = Student()
Student()
ss = Student()
s2 = Student()
print(Student.count)

ex.2
class Student:
    count = 0
    def __init__(self):
        print("enter into constructor")
        Student.count += 1
[Student(), Student(), Student(), Student(), Student(), Student()]
print(Student.count)
"""

"""
ex. program to count how many reference does object have
import sys

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Raju")
print(sys.getrefcount(p1))   # kuch number aayega, but expected se 1 zyada

Note :
1. it will give you reference count as two because internally when we call sys.getrefcount(p1) so in from the end of getrefcount(x) suppose there is a local variable who also points p1 so x = p1.
"""

"""
# how can we count how many object live in ram or how many objects are created by a developer

class Demo:
    Tol_obj_count = 0
    live_obj_count = 0
    def __init__(self):
        print("constructor hits")
        Demo.Tol_obj_count += 1
        Demo.live_obj_count += 1
    def __del__(self):
        print("destructor hits")
        Demo.live_obj_count -= 1

d1 = Demo()
d2 = Demo()
del d1
print("Total objects: ",Demo.Tol_obj_count)
print("live objects: ",Demo.live_obj_count)
"""

"""
# how weak object reference works in python

import weakref # this is one of the modules in python
class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"name: {self.name}")
        
p1 = Person("Raju")
weak_ref = weakref.ref(p1)
print(weak_ref)          # <weakref at 0x...; to 'Person' at 0x...>
print(type(weak_ref))    # <class 'weakref'>

ex.2
import weakref
import sys

class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"name: {self.name}")

p1 = Person("Raju")

# Normal reference
normal_list = [p1]
print(sys.getrefcount(p1) - 1)  # 2 (p1 + normal_list ke andar wala)

# Weak reference
weak_list = [weakref.ref(p1)]
print(sys.getrefcount(p1) - 1)  # 1 (sirf p1! weak reference count mein nahi aata)

ex.3
import weakref
import sys

class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"name: {self.name}")
        return self.name
    
# strong ref
p1 = Person("Raju")
# weak ref using weakref module
weak_ref = weakref.ref(p1)

# accessing instance attribute
k = p1.name
print(k)

# accessing instance attributes using weakref
# k = weak_ref.name # you can not by weak_ref
k = weak_ref().name # you can by calling weak_ref which gives you real instance address then you can call attributes
print(k)

ex.4
import weakref
import sys

class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"name: {self.name}")
        return self.name
# strong ref
p1 = Person("Raju")
# weak ref using weakref module
weak_ref = weakref.ref(p1)
# accessing instance attribute
k = p1.name
print(k)
del p1
# accessing instance attributes using weakref
# k = weak_ref.name # you can not by weak_ref
k = weak_ref() # you can by calling weak_ref which gives you real instance address then you can call attributes
print(k) # if real objects doesn't live in memory then weak_ref() returns None as result which tells us that object no longer present in ram

ex.5 calculates how many objects were created and how many of them still live in RAM
class Person:
    Total_objects = 0 # this only tells us how many objects till made by us
    live_objects = 0 # this tells us how many of them live in ram now
    def __init__(self):
        print("constructor called")
        Person.Total_objects += 1
        Person.live_objects +=1
        self.name = "kartik"

    def show(self):
        print(f"data : {self.name}")

    def __del__(self):
        print("destructor called")
        Person.live_objects -= 1

p1 = Person()
del p1
print(Person.Total_objects)
print(Person.live_objects)

ex.6
import weakref as weak
class Person:
    _instance = []
    def __init__(self):
        print("constructor called")
        Person._instance.append(weak.ref(self))
        self.name = "kartik"
        
    @classmethod
    def live_obj(cls):
        live_objects = [ref for ref in cls._instance if ref() is not None]
        return len(live_objects)
        
    def __del__(self):
        print("destructor called")

p1 = Person()
p2 = Person()
del p1
print(Person.live_obj())
"""
