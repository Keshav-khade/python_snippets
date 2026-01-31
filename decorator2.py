# python decorators 3 level architecture

"""
def add_prefix(prefix):
    def actual_deco(func):
        def wrapper(*args,**kwargs):
            print("welcome")
            return prefix + func(*args,**kwargs)
        return wrapper
    return actual_deco

@add_prefix("Mr. ")
def main_func(name):
    print("Thank you for using this function")
    return name

print(main_func("Kartik"))

"""

"""
# wapper function is you actual main function that you want to modify.
# when decorator have their own arguments you have to add another level or function which hold it's argument.
# always remember while working with *args and **kwargs you have to unpack these data structures.
# decorators are useful when you are working with many function that you have to modify back to back.
# decorator takes function as input and returns the function as output decorated function i mean.
"""