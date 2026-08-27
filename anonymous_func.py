# traditional function
"""
def sq(x):
   return x*x

n = int(input("Enter a number: "))
res = sq(n)
print("square is: ",res)
"""

"""
# now the same logic using single line lambda function
f = lambda x: x*x
n = int(input("Enter a number: "))
res = f(n)
print("square is: ",res)
"""

'''
# write a program to input two values and print the product of that two numbers
f = lambda a,b: a*b
# input two values using map lazy object
a, b = map(int, input("Enter two integers separated by space: ").split())
res = f(a,b)
print("product is: ",res)
'''

"""
# write a program to find the biggest of two values using lambda function
f = lambda x,y: x if x>y else y
val1, val2 = map(int, input("Enter values separated by comma: ").split())
res = f(val1, val2)
print(type(res))
print(f"the biggest value is: {res}")
"""

"""
# write a program to filter out even odd numbers

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

lst = [1,2,3,4,5,6,7,8,9,10]
res = list(filter(is_even, lst))
print(type(res))
print(res)
"""

'''
# the same program can be written in using lambda functions
lst = [1,2,3,4,5,6,7,8,9,10]
res = list(filter(lambda x:x%2 == 0, lst))
print(res)
'''

'''
def display_info():
    print("In function")

d=display_info    # d is function alias
print(id(display_info))
print(id(d))
d()
'''
