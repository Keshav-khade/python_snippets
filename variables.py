# this function show the variables inside functions
a = 2
"""
def variables():
          "this is the gobal and local variable scope"
          a = 3
          print("local variable a:",a)
variables()          
print("gloabal variable: ",a)


# now we wants to manupulate global from inside a funcion
def variables():
          "this is the gobal and local variable scope"
          global a
          a = 3
          print("local variable a:",a)
variables()          
print("gloabal variable: ",a)

# in the above code you just change keyword but local variable no more available how to fix this 
# using globals() funtion that returns the dictionary of global variables and you can assign it to another variable for you use
 

def variables():
          "this is the gobal and local variable scope"
          a = 3
          x = globals()['a']
          print("local variable a:",a)
          print("global variable:",x)
variables()          
print("gloabal variable: ",a)

"""
x = 10
y = 20

print(globals()) # globals() is a giant diction that contain build-in function and many more

#Global variable ko function ke andar access karna
x = 100
def test():
    globals()['x'] = 200 # for inline assingment python doesn't allows with global keywords
test()
print(x)

# globals() ek dictionary hai,aur dictionary kitne bhi variables handle kar sakti hai
#Multiple variables ko READ karna
a = 10
b = 20
c = "Python"
def show():
    g = globals()
    print(g['a'])
    print(g['b'])
    print(g['c'])

show()

#Multiple variables ko UPDATE karna
def update():
    g = globals()
    g['a'] = 100
    g['b'] = 200

update()
print(a, b)

#Multiple variables ek saath CREATE karna
def create():
    g = globals()
    g['x'] = 10
    g['y'] = 20
    g['z'] = 30

create()
print(x, y, z)