# decorators in python 
# decorators with parameters in python
"""
def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner

@changecase
def my_main(name):
    return "Hello "+ name

print(my_main("kartik"))

"""

"""
# when you call decorator always functions object will be passed.
# when you call wapper than actual function will be called.
# you can also return the functions reference to the other function to point that function.
# you can call any types and numbers of arguments in runtime by the help of *args & **kwargs
# * args is tuple and ** kwargs is dictionary.

# how closure property used here when remembering functions and their variables
Because Python does NOT delete variables that are still being used by another function.- called closure
If an inner function uses a variable from outer scope,
Python stores that variable inside the inner function object.

print(myfunction.__closure__) -> use this function to find the function object inside the closure.

"""

def changecase(func):
    def myinner(*args,**kwargs):
        return func(*args,**kwargs).upper()
    return myinner

@changecase
def my_main(name):
    return "hello "+name

print(my_main("kartik"))