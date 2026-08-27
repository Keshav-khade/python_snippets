#                                                 general class definition
'''
class student: # class student(object): both of these are same by default
        def __init__(self):
                self.name = input("Enter your name: ")
                self.age = int(input("Enter your age: "))
        def display(self):
                print(f"your name is: {self.name}")
                print(f"your age is: {self.age}")

obj = student()
student.display(obj)
'''
#                                                 class and object variables
'''
note: here school is called class variable both the object shares this variable from class you can change this variable also by using class name as: classname.varname/method() = "assignment"

class Student:
    school = "DPS"          # Line A

    def __init__(self, name):
        self.name = name    # Line B


s1 = Student("Raj")
s2 = Student("Amit")



when to use class variable:   when objects have fixed values
                              Objects counting
                              Configuration/constants

class Student:
    student_count = 0          # kitne students bane track karo
    MAX_MARKS = 100            # constant — kabhi nahi badlega

    def __init__(self, name):
        self.name = name
        Student.student_count += 1   # har object banne pe count badhe

s1 = Student("Raj")
s2 = Student("Amit")
print(Student.student_count)   # 2 — real production mein ye useful hai!


python lookup -> first it will check the objects and then it will check the class scope
-> you can change the object variables and methods and also class variables and methods by using object name and class name
-> when class variable changes so it will effect on all objects
-> when objects variable changes then it will stay in their scope only
-> our constructor can have more than one parameter

'''

'''
# accessing the class variable from inside the class
# accessing the class and instance variable from outside of the class


class Bank:
          bank_name = "SBI"
          rate = 8.5

          def __init__(self,holder,balance):
                  self.holder = holder
                  self.balance = balance

          def show(self):
                  print(f"bank name: {self.bank_name}")
                  print(f"bank interest rate: {self.rate}") # from inside the class
                  print(f"bank name: {self.holder}")
                  print(f"bank name: {self.balance}")
acc1 = Bank("Rahul",50000)
acc2 = Bank("haru",40000)

Bank.rate = 9.0
acc1.rate = 99
print("\n--- After acc1.interest_rate = 99 ---")
print(acc1.rate)   # kya aayega?
print(acc2.rate)   # kya aayega?
print(Bank.rate)   # kya aayega?

'''

'''
# accessing and modifying class and instance variable from outside of the class

⚠️ But ye dangerous bhi hai — dekho kyun:
pythons1.garde = "A"    # typo! "grade" ki jagah "garde" likha
print(s1.grade)   # ❌ AttributeError — kyunki "garde" bana tha!
Koi error nahi aaya jab banaya — silently wrong variable ban gaya! Isliye production mein bahar se random variables add karna avoid karte hain.


class Student:
          school = "DPS"

          def __init__(self,name,marks):
                  self.name = name
                  self.marks = marks
s1 = Student("ram",87)

# accessing the methods
print(s1.name)
print(Student.school)

# modifying from outside
s1.name = "raju"
Student.school = "orchid"

# after modification
print(s1.name)
print(s1.school)
print(Student.school)

# adding new variable from outside
s1.grade = "A"
print(s1.grade)
'''

'''
notes: classmethod ko object se bhi call kar sakte hai and class name se bhi but jab object se karte hai to koi naya object member create nhi hota or self pass nhi hota instead entire class and address cls me pass hota hai .

Object se instance variable access✅ s1.name
Object se instance method call✅ s1.display()
Object se class variable access✅ s1.school — class se utha lega
Object se classmethod call✅ s1.change_school() — class change hogi
Class se class variable access✅ Student.school
Class se classmethod call✅ Student.change_school()
Instance variable modify✅ Sirf us object pe effect
Class variable modify✅ Saare objects pe effect


class student:
          school = "dps"
          cur_student = 0

          def __init__(self,name,age):
                  self.name = name
                  self.age = age
                  student.cur_student += 1

          def show(self):
                  print(f"{self.name}")
                  print(f"{self.age}")

          @classmethod
          def change_school(cls,new_school):
                  cls.school = new_school

          @classmethod
          def get_count(cls):
                  print(f"{cls.cur_student}")

s1=student("raj",21)
s2=student("kar",22)
s3=student("ram",23)

s1.show() # student.show(s1)
s2.show()
s3.show()

student.change_school("harvard international") # student.change_school(student)
s1.change_school("Ips school") # student.change_school(student,"ips school")
student.get_count()

print(student.school)
print(s1.school)
print(s2.school)
print(s3.school)

# this is the way you would know namespaces
print(s1.__dict__)
print(student.__dict__)
'''

'''
when we try to access class variable or class namespace from object
Q1 — s1.school karte hain toh kya?

Ye lookup order ka kaam hai — copy share nahi hoti!
Ye common misconception hai — actually hota ye hai:

pythonprint(s1.school)   # "DPS"

Python ne kya kiya internally:
        │
        ▼
s1.__dict__ mein dhundha — {"name": "Raj", "age": 21}
        │
   nahi mila!
        │
        ▼
Student.__dict__ mein gaya — {"school": "DPS", ...}
        │
     mila! "DPS" return kiya

Copy share nahi hoti — Python sirf class mein jaake value padhta hai!

Object ke paas apna school hota hi nahi jab tak explicitly set na karo!

'''


'''
Q2 — Methods kis namespace mein hote hain?

Ye bhot acha socha! 🎯

Dono — normal method aur classmethod — Class ke namespace mein hote hain!

pythonprint(Student.__dict__)
# {'school': 'DPS',
#  '__init__': <function>,   ← normal method — class mein!
#  'display': <function>,    ← normal method — class mein!
#  'change_school': <classmethod>}  ← classmethod — class mein!

print(s1.__dict__)
# {'name': 'Raj', 'age': 21}
# ← koi bhi method nahi! sirf data!

Koi bhi method — normal ho ya classmethod — object ke namespace mein kabhi nahi hota!

Kyun? — Memory efficiency! 🔑

Socho agar 1000 students banaye:

❌ Galat approach — methods object mein
s1.__dict__ = {name, age, display, result, change_school...}  ← 1000 copies!
s2.__dict__ = {name, age, display, result, change_school...}  ← 1000 copies!
... 1000 objects = 1000 copies of same methods — waste!

✅ Sahi approach — methods class mein
Student.__dict__ = {display, result, change_school}  ← sirf ek copy!
s1.__dict__ = {name, age}   ← sirf data!
s2.__dict__ = {name, age}   ← sirf data!
Isliye methods hamesha class ke namespace mein hote hain — ek hi copy, saare objects use karte hain!

'''