"""
Aggregation :
1. when there is possibilities of creating contained object without a container object, which means container object weakly related or associated with contained object.
2. one object uses another object
3. if container object is destroyed then contained object still exists in memory
4. weak has-a relationship between objects
5.The container uses another object, but it does not own its entire life cycle.
6. when two or more classes can exists indepen

"Why is aggregation considered a weaker relationship than composition?"
Answer:
In composition, the parent controls the child object's creation and lifetime.
In aggregation, the child object exists independently and can be shared.

Composition  "I create it."
self.engine = Engine()

Aggregation  "I receive it."
self.engine = engine


"""

"""
class Library:
    def __init__(self, name):
        print("Library constructor")
        self.name = name
        self.book_list = []

    def add_books(self,*book):
        book_ref = book
        for book in book_ref:
            self.book_list.append(book)

    def get_books(self):
        for ind in range(len(self.book_list)):
            print(f"------ book{ind+1}------")
            self.book_list[ind].show()

class Book:
    def __init__(self, author, genres):
        print("book created")
        self.auth_n = author
        self.genres = genres

    def show(self):
        print(f"book author: {self.auth_n}\nbook genres: {self.genres}")

b1 = Book(author = 'sudha murti',genres = 'self help')
b2 = Book("steve jobs","biography")
b3 = Book("Lord krishna", "infinit knowledge")

l1 = Library("Indian knowledge")
l1.add_books(b1,b2,b3)
l1.get_books()

"""

"""
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []   # khaali list — abhi koi employee nahi

    def add_employee(self, emp):
        self.employees.append(emp)   # ✅ AGGREGATION — bahar se bana object add ho raha hai


# Employee object BAHAR bana — Department ke bina bhi yeh exist kar sakta hai
e1 = Employee("Raju")

d1 = Department("Engineering")
d1.add_employee(e1)   # existing object ko department mein "assign" kiya

# Ab agar department khatam ho jaaye:
del d1
print(e1.name)   # ✅ "Raju" — employee OBJECT ABHI BHI ZINDA HAI!
                  # kyunki e1 apna independent reference rakhta hai, Department se juda nahi
"""

