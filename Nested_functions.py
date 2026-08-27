"""
def show():
    print("in show functon")
    print("2nd line of show function")
    def display():
        print("in display function")
        print("second line of display function")
    print("3rd line of show funcion")
    display()
    print("Last line of show function")
"""

'''
def outer():
    def inner():
      print("Hello from inner")
    inner()
outer()


def outer(x):
    def inner():
      print("the value of x is :",x)
    inner()
x = 10
outer(x)


def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1 
    increment()
    increment()
    increment()
    print("final count is :",count)
counter()
'''

'''
# closure property in functions
def make_multiplier(n):
        def multiplier(x):
            return x * n
        return multiplier
double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))
print(triple(5))
'''

"""
# recursive logic with nested functions
def factorial(n):
        fact = 1
        def helper(n):
                if n==0:
                  return 1
                nonlocal fact
                fact = fact * n
                helper(n-1)
        helper(n)
        print("factorial of a number is:",fact)
n = int(input("Enter a number: "))
factorial(n)
"""

"""
UnboundlocalError : x is not assigned yet 
def outer():
    x = 5
    def inner():
        x = x + 1   # <-- yahan problem hai
        print(x)
    inner()
outer()
"""

"""
# nested helper() for prime number checking
def is_prime_list(numbers):
        lst = []
        def is_prime(val):
            if val <= 1:
                return False
            for i in range(2,val):
                if val % i == 0:
                    return False
            return True
        for val in numbers:
            if is_prime(val):
                lst.append(val)
            else:
                continue
        return lst

lst = [-1,5,-6,11,13,17,19,23]
lst = is_prime_list(lst)
print(lst)
"""