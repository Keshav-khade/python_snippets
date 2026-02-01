"""
a function without a name is called lambda function and hence it called the anonymous function also 
we can pass and returned lambda functions to another function
lambda functino can be take any number fo arguments but have only one expression
you can use it with filter() , map() , reduce() , sorted() methods also
syntax ->{ lambda argument: expression }

"""

#comparison b/w simple function Vs lambda
def add(a,b):
          return a+b

x = lambda a,b: a+b # lambda doesn't have names itself so we can refered using any names, this helps in calling phase
print(add(5,5))
print(x(5,6)) 

# simple snippets for better understanding
f = lambda x: x*x
"this function finds the square root of x"
print(f(5))

fun = lambda x,y: x if x>y else y
"this function finds the larger number here"
print(fun(5,6)) # remember the positional arguments x takes 5 and y takes 6 here

fun = lambda x: x+10
"add a number with 10 and returned the sum"
print(fun(5))

# some arithmatic problems
lst = [lambda x,y: x*y,
lambda x,y: x+y,
lambda x,y: x-y,
lambda x,y: x/y,
lambda x,y: x//y,
lambda x,y: x**y
]
x=10
y=3
lst1 = []
for i in lst:
        lst1.append(i(x,y))
print(lst1)


# the pythonic way to write preceding code
result = [i(x,y) for i in lst]
print(result)

# here is the another way to do it with the help of dictionaries
operations = {"multiply":lambda x,y: x*y, 
          "addition":lambda x,y: x+y,
          "subtraction":lambda x,y: x-y,
          "division":lambda x,y: x/y,
          "floor division":lambda x,y: x//y,
          "power":lambda x,y: x**y}
x = 10
y = 3
print(type(operations))
result = {}
for name , value in operations.items():
        result[name] = value(x,y)
print(result)        


# with the help of dictionary comprehension
result = {name:value(x,y) for name,value in operations.items()}
print(result)

# Why Use Lambda Functions?
"""
The power of lambda is better shown when you use them as an anonymous function inside another function.
"""

def myfunction(n):
        return lambda a:a*n

my_main = myfunction(2)
my_main1 = myfunction(3)

print(my_main(11))
print(my_main1(11))

# from now onward we will see how to use lambda function in data analytics and with build-in functino that takes lambda as a input to perform some tasks

"""
1. map() -> Applies a function to each element
          Returns a map object (convert to list)
2. syntax -> map(function, sequences)  
3. you can have 1 function and one or more sequences
4. you can use one function only but have multiple sequences and for every sequence you have to map one argument if you using lambda of regular function 

"""

def square(x):
        return x*x
lst = [1,2,3,4,5]
lst1 = list(map(square,lst))
print(lst1)

# the previous code using lambda function
lst1 = list(map(lambda x: x*x , lst))
print(lst1)

# more than one sequences
lst1 = [10,20,30,40,50,60]
lst2 = list(map(lambda x,y: x*y , lst , lst1))
print(lst2)

# map with three sequences
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
result = list(map(lambda x, y, z: x + y + z, a, b, c))
print(result)

# map with multiplse function so it's possible using workaround takes a list of functions for any sequencial container
funcs = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x ** 2
]
value = 5
result = list(map(lambda f: f(value), funcs))
print(result)

# here lambda works same as below function internally this logic lambda f: f(value), work like this
result = []
for f in funcs:
    result.append(f(value))

# function with mutiple function and values
funcs = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x ** 2
]
value = [1,2,3]
result = list(map(lambda f , v: f(v), funcs , value))
print(result)
