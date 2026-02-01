# python snippet for recursive function
# this is the recursive approach of calculating the factorial of a number
def factorial(n):
          "this function calculate factorial of a number"
          if n==0:
                  result = 1
          else:
                  result = n * factorial(n-1)
          return result
print("here we are providing some numbers: ")
for i in range(1,11):
        print("factorial of {} is {} ".format(i,factorial(i)))
              