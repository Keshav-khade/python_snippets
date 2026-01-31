#  function in python
# a python program to see how to assign a function to a variable.

def display(name):
    " this function greets the user "
    return "Hai "+name
x = display("kartik")
print(x)



# function inside function
def display(str):
    def message():
        return "how are you ?"
    result = message() + str
    return result
print(display("kartik"))


# function as a parameter
def display(func):
    " this function displays the greeting but we pass function as a parameter"
    return "hey" + func
def message():
    return "How are you? "
print(display(message()))



# functions can return functions also
def greet():
    def message():
        return " how are you ? "
    return message
func = greet()
print(func())



        

