# python generators
"""
generators -> gener. are the functions and they can be written as ordinarty function but the difference is in their return statement while in ordinary function we write return but here we have to write 'yield'.

A generator can be iterated only once.
After that, its empty forever.

A generator:
Produces values one at a time
Remembers its state
Cannot be reset or reused once exhausted

"""
# simple sinppet here generator generates numbers from x to y 
def mygen(x,y):
          while x <= y:
                  yield x
                  x += 1
g = mygen(5,10)
print(type(g))
# this is how you can print generated values
"""
for i in g:
        print(i,end=",")
"""
# another way is convert in into list or any iterable and then print
lst = list(g)
print(lst)


# now we can understand yield function clearly 
def normal_func():
    "this is the simple func to show behavior of return"
    print("Function start")
    return 1
    print("This will never run")
print(normal_func())

# now what yield statement does
def mygen(x, y):
    "this program demonstrate how yield statement works" 
    print("Generator started")
    while x <= y:
        print("Before yield, x =", x)
        yield x
        print("After yield, x =", x)
        x += 1
    print("Generator finished")
g = mygen(5, 7)
print("Generator object created")
for i in g:
    print("Received value:", i)


# you can also check manually using next() or __next__()
g = mygen(1, 3)

print(next(g))
print("-----")

print(next(g))
print("-----")

print(next(g))
print("-----")

print(next(g,"hey stop"))  # Uncomment → StopIteration error


# generates the number from 1 to n
def mygen(x,y):
    print("start")
    while x <= y:
        print("value before yield:",x)
        yield x
        print("value after yield:",x)
        x += 1
n = int(input("Enter the ending range: "))
g = mygen(1,n)
for i in g:
    print("received: ",i)


# even number generator
def even_num(n):
    i = 1
    while i<=n:
        if i % 2 == 0:
            yield i
        i += 1
g = even_num(10)
lst = list(g)
print(lst)

# generating list element one by one , you can also say unpacking the list object using yield 
def lst_gen(lst):
    for i in lst:
        print("before: ",i)
        yield i
        print("after:",i)
for i in lst_gen([1,2,3,4]):
    print("received: ",i)


# using yield without loop , uses recursion but it's harmful for large range (~100000)
"""
yield from gen , this line help you to call function itself means recursive call
internally python interprets as 

for value in gen:
    yield value
"""

def even_gen(n, i):
    if i > n:
        return
    if i % 2 == 0:
        yield i
    yield from even_gen(n, i + 1)
g = even_gen(10,1)
print(list(g))