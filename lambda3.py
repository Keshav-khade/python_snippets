"""
reduce() -> a reduce() func process a sequence and returns a single number from sequence of elements accroding to the function which passed to reduce.
1. syntax -> reduce(function,iterable,initializer)
2. make sure you import this function from functools module 
as from functools import * (or you can use reduce as well)

reduce ->
Apply a function of two arguments cumulatively to the items of a sequence
or iterable, from left to right, so as to reduce the iterable to a single
value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
((((1+2)+3)+4)+5). If initial is present, it is placed before the items
of the iterable in the calculation, and serves as a default when the
iterable is empty.

notes :
          Parameters:
          function :function that takes two arguments and returns a single value.
          iterable :sequence (list, tuple, etc.) whose elements will be processed.
          initializer :(optional) A starting value. If provided, it is placed before the items of the iterable in the calculation.
"""
# snippets for better understanding
from functools import *
lst = [1,2,3,4,5]
lst1 = reduce(lambda x,y:x*y,lst)
print(lst1)

# you can use your custom function also 
def add(a,b):
          return a+b
lst1 = reduce(add,lst)
print(lst1)

# calculating or summarize values from 1 to 50 using reduce
lst2 = reduce(lambda x,y:x+y,range(1,51)) # here range will itself generates the value and you know that range function return it's own data type range() and you can convert it to any data type.
print(lst2)

# how to use initializer with sum
numbers = [1, 2, 3]
result = reduce(lambda x, y: x + y, numbers, 10)
print("Sum with initializer:", result)  # Output: 16

# small snippets 
numbers = [2, 4, 6]
product = reduce(lambda x, y: x * y, numbers)  # ((2 x 4) x 6) = 8 x 6 = 48
min_value = reduce(lambda x, y: x if x < y else y, numbers) # 2

words = ['dog', 'cat', 'tree', 'pony']
str_concat = reduce(lambda x, y: x + y, words)  # "dogcattreepony

print(product)
print(min_value)
print(str_concat)

"""Initializer Without an initializer, reduce() takes the first element of the iterable as its starting value. If the iterable is empty, reduce() throws a TypeError. To make code robust, supply an initializer to define behavior on empty input."""

