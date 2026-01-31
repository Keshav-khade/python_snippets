# passing a group of element to a function

def calculate(lst):
          "here we pass some number"
          n = len(lst)
          sum = 0
          avg = 0
          for i in lst:
                  sum += i
          avg = sum / n
          return sum , avg

print("enter some number: ")
lst = [int(i) for i in input().split()]
x,y=calculate(lst)        
print(f"your sum is:{x}")                  
print(f"your avg is:{y}")

"""
here split function returns a list of string
.split() -> default version separate a string based on whitespace, comma , \n ,\t
.split(sep=" ") -> explicitly we are saying that separate based on one space charactor

input() -> this function takes a string as input even user types some number then it uses split funciton

"""

# same logic works or string also
def display(lst):
        "displays the provided string"
        for i in lst:
                print(i)
print("enter a string separated by comma: ")
lst = [x for x in input().split(",")]

display(lst)

        