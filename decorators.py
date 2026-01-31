# decorators in python

def deco(func):	#decorator function
    def inner(num):
        if num <= 0:
            return
        return func(num)
    return inner

@deco
def my_main(num):	#decorated function
    return num * num

print(my_main(-5))
print(my_main(7))



# if you use *args , **kwargs then your facing problem with tuple and dictionaries for that use can use this logic to unpack them
'''
def validate_positive(func):
    def wrapper(*args, **kwargs):
        for val in args:
            if isinstance(val, int) and val < 0:
                print("Negative value not allowed")
                return

        for val in kwargs.values():
            if isinstance(val, int) and val < 0:
                print("Negative value not allowed")
                return

        return func(*args, **kwargs)
    return wrapper
'''