"""
from sys import getrecursionlimit , setrecursionlimit
def show():
    print("In show")
    print("Thank you")
    show()
print("default recursion limit is: ",getrecursionlimit())
setrecursionlimit(500)
print("default recursion limit is: ",getrecursionlimit())
show()

"""

'''
# factorial of a number using for loop
prod = 1
def fact(x):
   for i in range(1, x+1):
      global prod
      prod = prod * i
   return prod
n = int(input("Enter a number: "))
res = fact(n)4
print(f"factorial of {n} is {res}")

'''

"""
# factorial of a number using recursion
def fact(x):
  # base case
  if x == 1:
    return 1
  return x * fact(x-1) 

n = int(input("Enter a number: "))
res = fact(n)
print(f"factorial of {n} is {res}")
"""

"""
# Example 4: Write a program to input n value. Display sum of individual digits of a number using recursion?
def total(x):
   #base case
   if x == 0:
      return 0
   rem = x % 10
   x = x // 10
   return rem + total(x)
    
n = int(input("Enter a number: "))
res = total(n)
print(f"sumation of {n} is {res}")
"""

"""
#Example 5: Write a program to input n value. Display reverse of that number using recursion?
def reverse(x,rev=0):
   # base case
   if x == 0:
      return rev
   rem = x % 10
   x = x // 10
   rev = rev * 10 + rem
   return reverse(x,rev)

n = int(input("Enter a number: "))
res = reverse(n) # 1234
print(f"reverse of {n} is {res}")
"""

