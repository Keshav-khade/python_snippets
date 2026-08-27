# wap to print n natural numbers using for loop construct
'''
n = int(input())
for i in range(1,n+1):
          print(i,end=" ")

'''
#                                                 patterns
'''
1.
          * 
          * * 
          * * * 
          * * * * 
          * * * * * 

n = int(input())
for i in range(1,n+1):
          for j in range(i):
                  print("*",end=" ")
          print()
'''

'''
2. odd number of starts
          * 
          * * * 
          * * * * * 
          * * * * * * * 
          * * * * * * * * *          

n = int(input())
for i in range(1,n+1):
          for j in range(2*i-1):
                  print("*",end=" ")
          print()         
'''
'''
3. right stars:
                            * 
                          * * 
                        * * * 
                      * * * * 
                    * * * * *

n = int(input())
for i in range(1,n+1):
          for j in range(n-i):
                  print(" ",end=" ")
          for j in range(i):
                  print("*",end=" ")
          print()


n = int(input())
for i in range(1,n+1):
          for j in range(n):
                    if j < n-i:
                          print(" ",end=" ")
                    else:
                          print("*",end=" ")
          print()
'''

'''
4. pattern for pyramid
                        * 
                       * * 
                      * * * 
                     * * * * 
                    * * * * *
n = int(input())
for i in range(1,n+1):
          for j in range(n-i):
                  print(" ",end="")
          for j in range(i):
                  print("*",end=" ")
          print()

'''

'''
5. downward pyramid
                    * * * * * 
                     * * * * 
                      * * * 
                       * * 
                        * 
n = int(input())
for i in range(n):
          for j in range(i):
                  print(" ",end="")
          for j in range(n-i):
                  print("*",end=" ")
          print()
'''

"""
patter printing:
A 
A B 
A B C 
A B C D 

A = 65
# for rows
r = int(input("Enter the number of rows needed: "))
for i in range(r):
    for j in range(i+1):
        print(chr(A+j), end=' ')
    print()
"""

