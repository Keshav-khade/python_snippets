"""
def modify(x):
     x = x + 5
     print(x," ",id(x))
x = 10
modify(x)
print(x," ",id(x))
"""

"""
def modify1(lst):
     "modifying the list not create new object"
     lst.append(9)
     print(lst," ",id(lst))
lst = [1,2,3]
modify1(lst)
print(lst, id(lst))
"""

"""
def modify1(lst):
     "modifying the list not create new object"
     lst = [10,12,13]
     print(lst," ",id(lst))
lst = [1,2,3]
modify1(lst)
print(lst, id(lst))
"""

"""
a= 1
def myfun():
   a = 2
   print("a is a local variable",a)
   print("a is a global variable",globals()["a"])

myfun()
print("a is in global scope",a)
"""

"""
def myfunction(lst):
          sum = 0
          for i in lst:
                  sum += i
          return sum/len(lst) , sum

lst = [int(i) for i in input().split()]
x,y = myfunction(lst)
print(f"avg is {x} and sum is {y}")
"""