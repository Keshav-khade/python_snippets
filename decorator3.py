# python decorators


def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
    def myinner():
        return "Hello " + func() + " Have a good day!"
    return myinner

@changecase
@addgreeting
def myfunction():
    return "Tobias"

print(myfunction())

"""
# here the main part is @ wala part 
python internally interprets this as @  myfunction = change(addgreeting(myfunction))
# here the actual mapping of function is done. this is called the decoration phase where the flow of execution is bottom to top
# inner function maps first then outermost then so on.

now,
second phase is calling phase, where we call the outermost decorator first then inner functions and then inner function so on.
# now the bottom most means main function who is getting modified returns the data and then flow again goes upward which is bottom to top level and last most decorator return the modified value.

& general decorator phase in case of multiple decorator calls :>  main_fun = A(B(C(main_fun)))
& general calling phase :>  main_fun() -> C() -> B() -> A() ->  o\\p.
"""
