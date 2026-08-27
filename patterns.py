n = int(input("Enter a number: "))
# from math import factorial
"""
for i in range(1,n):
          print("i=",i,end="\n")
          for j in range(1,n):
                    print("\tj=",j,end="")
          print()
"""

"""
for i in range(1,n):
          print("i=",i,end="\n")
          for j in range(n-1,0,-1):
                    print("\tj=",j,end="")
          print()
"""

"""
for i in range(1,n):
          for j in range(1,n):
                  if i == j:      
                    print("i= ",i," ","j= ",j)
"""

"""
for i in range(1,n):
          for j in range(1,n):
                  if i != j:      
                    print("i= ",i," ","j= ",j)
"""

"""
for i in range(1,n):
          for j in range(1,n):
                  if i == j:
                    break      
                  print("i= ",i," ","j= ",j)
"""

"""
for i in range(1,n):
          for j in range(n-1,0,-1):
                  if i == j:
                    break      
                  print("i= ",i," ","j= ",j)
"""

"""
for i in range(1,n):
          for j in range(n-1,0,-1):
                  if i == j:
                    continue      
                  print("i= ",i," ","j= ",j)
"""

"""
1.        1
          12
          123
          1234
          12345

for i in range(1,n):
          for j in range(1,i+1):
                  print(j,end="")
          print()

x = 0       
for i in range(1,n):
          x = x*10+i
          print(x)
"""

"""
2.        1
          22
          333
          4444
          55555

for i in range(1,n+1):
          for j in range(1,i+1):
                  print(i,end='')
          print()
"""

"""
2.        55555
          4444
          333
          22
          1


for i in range(n,0,-1):
          for j in range(i):
                  print(i,end='')
          print()
"""

"""
3.        12345
          1234
          123
          12
          1  

for i in range(n,0,-1):
          for j in range(1,i+1):
                  print(j,end='')
          print()
"""

"""
4. floyd's triangle
          1 
          2 3 
          4 5 6 
          7 8 9 10 
          11 12 13 14 15

x=1
for i in range(n):
          for j in range(i+1):
                    print(x,end=" ")
                    x += 1
          print() 
"""

"""
6. slides triangle
          1
          01
          101
          0101
          10101

for i in range(1,n+1):
          for j in range(i):
                  print((i+j)%2,end='')       
          print() 


for i in range(n+1):
          num = i % 2
          for j in range(i):
                    print(num,end='')
                    num = 1 - num
          print()

for i in range(n,0,-1):
          for j in range(i,6):
                    print(j%2,end='')
          print()
"""

"""
7.        12345
          23451
          34512
          45123
          51234
          12345

for i in range(1,7):
          for j in range(i,6):
                  print(j,end='')
          for k in range(1,i):
                  print(k,end='')
          print()
"""

"""
8.        12345
           2345
            345
             45
              5

for i in range(1,n+1):
          for j in range(1,i):
                  print(" ",end='')
          for j in range(i,n+1):
                  print(j,end='')
          print()


for i in range(1,6):
          print(end=" "*(i-1))
          for j in range(i,6):
                  print(j,end='')
          print()
"""

"""
9.
              1
             121
            12321
           1234321
          123454321


for i in range(1,n+1):
          print(end=' '*(n-i))
          for j in range(1,i):
                  print(j,end='')
          for j in range(i,0,-1):
                  print(j,end='')
          print()

"""

"""
10.     123454321
         1234321
          12321
           121
            1      

for i in range(n,0,-1):
        print(end=' '*(n-1))
        for j in range(1,i):
                print(j,end='')
        for j in range(i,0,-1):
                print(j,end='')
        print()
"""

'''
11.                 1
                   121
                  12321
                 1234321
                123454321
                 1234321
                  12321
                   121
                    1

for i in range(1, n):
    print(end=" " * (n - i))
    for j in range(1, i):
        print(j, end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()
for i in range(n, 0, -1):
    print(end=" " * (n - i))
    for j in range(1, i):
        print(j, end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()

'''
'''
12.       * 
         * * 
        * * * 
       * * * * 
      * * * * * 
     * * * * * * 
      * * * * * 
       * * * * 
        * * * 
         * * 
          * 
for i in range(1, n+1):
    print(end=" "*(n-i))
    for j in range(i):
        print("* ", end='')
    print()
for i in range(n, 0, -1):
    print(end=' '*(n-i+1))
    for j in range(i, 1, -1):
        print("* ", end='')
    print()
'''
'''
13.      * 
        * * 
       *   * 
      *     * 
     *       * 
    *         * 
     *       * 
      *     * 
       *   * 
        * * 
         * 
         
for i in range(1, n+1):
    print(end=" "*(n-i))
    for j in range(i):
        if i == 1:
            print("* ", end='')
        else:
            if (j == 0) or (j == i-1):
                print("* ", end='')
            else:
                print("  ", end='')
    print()

for i in range(1, n):
    print(end=' '*i)
    for j in range(n-i, 0, -1):
        if i == n-1:
            print("* ", end='')
        else:
            if (j == n-i) or (j == 1):
                print("* ", end='')
            else:
                print("  ", end='')
    print()
'''
'''
14. 1234554321
    1234  4321
    123    321
    12      21
    1        1
    12      21
    123    321
    1234  4321
    1234554321
    
spaces = 0
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end='')
    print(' ' * spaces, end='')
    spaces += 2
    for j in range(i, 0, -1):
        print(j, end='')
    print()
spaces -= 4
for i in range(2, n+1):
    for j in range(1, i+1):
        print(j, end='')
    print(' ' * spaces, end='')
    spaces -= 2
    for j in range(i, 0, -1):
        print(j, end='')
    print()  
'''

'''
15.
# # # # # # # 
#           # 
#           # 
#           # 
#           # 
#           # 
# # # # # # # 

n = int(input())
spaces = 0

for i in range(1,n+1):
    if i == 1 or i == n:
        for j in range(1,n+1):
            print("# ",end='')
        print()
    else:
        for j in range(1,n+1):
            if j==1 or j==n:
                print("# ",end='')
            else:
                print("  ",end='')
        print()
'''

'''
16.
# # # # # 
      #   
    #     
  #       
# # # # # 

for i in range(1, n+1):
    if i == 1 or i == n:
        for j in range(1, n+1):
            print("# ", end='')
        print()
    else:
        for j in range(1, n+1):
            if j == n-i+1:
                print("# ", end='')
            else:
                print("  ", end='')
        print()
'''

'''
17. 
8 
8 6 
8 6 4 
8 6 4 2 
8 6 4 2 0 

for i in range(5):
    x = n
    for j in range(i+1):
        print(x, end=' ')
        x -= 2
    print()
'''

'''
18.
    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 

for i in range(n):
    print(end=" "*(n-i-1))
    for j in range(i+1):
        v = factorial(i) // (factorial(j) * factorial(i-j))
        print(v, end=' ')
    print()
'''

'''
19.
1 
2 b 
3 c 3 
4 d 4 d 
5 e 5 e 5 
6 f 6 f 6 f 

for i in range(1, n+1):
    if i % 2 == 0:
        for j in range(1, i+1):
            if j % 2 == 0:
                print(chr(97+i-1), end=' ')
            else:
                print(i, end=' ')
        print()
    else:
        for j in range(1, i+1):
            if j % 2 == 0:
                print(chr(97+i-1), end=' ')
            else:
                print(i, end=' ')
        print()
        

for i in range(1, n + 1):
    row = []

    if i % 2:  # odd row
        num = i
        ch = chr(ord('a') + i -1)

        for j in range(i):
            row.append(str(num) if j % 2 == 0 else ch)

    else:  # even row
        num = i
        ch = chr(ord('a') + i - 1)

        for j in range(i):
            row.append(ch if j % 2 == 0 else str(num))

    print(" ".join(row))
'''
