# functions in python
'''
def greet():
  return 'Hello sir'

x = greet  # funtion's object here x refers the greet function in this time.
print(x())

'''


# funtion can also be a input for other functions for example
'''
def my_func(func):
  return func()  # here you call another function by using another name, and you can.

def greet():
  return 'hello sir' # finally function greet() returns the value.

print(my_func(greet)) # here you pass function as a argument, yes you can.

'''

# functions return functions also
'''
def outer():
    def inner():
        return "hello I'm kartik"
    return inner 

here this is a object of function inner you can return object means function ka reference return hota hai \
function call nhi.

k = outer() # here k refers the function inner() function now 
print(k())	# here you call the inner functionS

'''

# in function closure how to works
'''
def outer():
    x = 10
    def inner(): #here inner function remembers the x variable even after the outer loop ends called closure property
        return x
    return inner

f = outer()
print(f())

'''


# 


