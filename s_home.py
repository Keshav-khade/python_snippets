"""
question 1. wap to separate alphabets and digits from a string
s = 'c1o2m3p4u5t6e7r8'
characters = ''
digits = ''

# first logic
for i in s:
    if i.isalpha():
        characters += i
    elif i.isdigit():
        digits += i

# second logic
for ch in s:
    if 65 <= ord(ch) <= 90:
        characters += ch
    elif 97 <= ord(ch) <= 122:
        characters += ch
    else:
        digits += ch

print(characters)
print(digits)
"""

"""
The actual execution order
For every generator/list comprehension with this shape:
pythonEXPRESSION for VAR in ITERABLE if CONDITION
Python processes it in this exact order, per item:

for — pull the next item from the iterable
if — test the condition on that item; if False, skip it entirely and go back to step 1
EXPRESSION — only if the condition passed, compute the expression and produce it
"""

"""
# find the acronym of a string

s = 'Bharat Heavy Electrical Limited'

acro = "".join(word[0].upper() for word in s.split())
print(acro)

s = 'Ministry of Home Affairs'
skip_word = {'of', 'and', 'the', 'for'}
lst_of_string = (word[0].upper() for word in s.split() if word.lower() not in skip_word)
acronym = "".join(lst_of_string)
print(acronym)
"""

"""
wap to input a string with spaces display acronym of a given string with last words all characters

s = 'Lal Bahadur Stadium'
lst_split = s.split()

ex_lst = [word[0] if ind < len(lst_split)-1 else word for ind, word in enumerate(lst_split)]
print(ex_lst)

final_s = "".join(ex_lst[:-1]) + " " + ex_lst[-1]
print(final_s)
"""

"""
write a program to find replication of a string 
for example s = "x3a4" -> output should be xxxaaaa

s = 'x3a5y4'

# get output with slicing with for loop
c = s[0::2]
d = s[1::2]
final_s = ''
for i in range(len(c)):
    final_s += c[i] * int(d[i])

print(final_s)

# using one for loop
result_s = ""
for i in range(0, len(s), 2):
    letter = s[i]
    digit = int(s[i+1])
    result_s += letter * digit

print(result_s)

# using generator logic with join()
res_s = "".join(s[i] * int(s[i+1]) for i in range(0, len(s), 2))
print(res_s)
"""

"""
wap to count the frequency of each word in string

s = 'the cat sat on the mat that cat is mad'
s = s.split()
freq = dict()

for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
"""

"""
#          Bubble sort

lst = [12, 34, 11, 8]
n = len(lst)
# print(lst)

for p in range(n-1):
    for i in range(n-p-1):
        if lst[i] > lst[i+1]:
            temp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = temp

print(lst)
"""

"""
quiz : take user input and calculate total amount and average price

lst = list()
n = int(input("Enter number of elements: "))

for i in range(n):
    obj = int(input("Enter values: "))
    lst.append(obj)

add = 0
avg = 0

for val in lst:
    add += val
avg = add / len(lst)

print(f"your sum: {add}\nyour average is: {avg}")

"""

"""
quiz: find the biggest and smallest element in an list

lst = [42, 17, 89, 3, 56, 91, 8, 23, 67, 91, 5]

big_val = lst[0]
small_val = lst[0]

for i in range(1, len(lst)):
    if lst[i] > big_val:
        big_val = lst[i]
    if lst[i] < small_val:
        small_val = lst[i]

print(f"your biggest element would be: {big_val}\nyour smallest element would be: {small_val}")
print(f"biggest: {max(lst)}, smallest: {min(lst)}") <- this will also gives you same result
"""

"""
quiz: find the frequency of each word in a list same goes for string and any other data structure

# time complexity of this approach is o(n)
lst = [4, 2, 7, 4, 9, 2, 4, 1, 7, 9, 4, 2]
n = len(lst)
freq = {}
for i in range(n):
    count = 0
    k = 0
    for j in range(n):
        if lst[i] == lst[j]:
            count = count + 1
            if j < i:
                k = k + 1
    if k == 0:
        freq[lst[i]] = count
print(freq)

# time complexity of this appraoch is 0(n^2)
freq = {}
for i in range(len(lst)):
    if lst[i] in freq:
        freq[lst[i]] = freq[lst[i]] + 1
    else:
        freq[lst[i]] = 1
print(freq)

# third approach with .get(value , default) method of dictionary
freq = dict()
for i in range(len(lst)):
    freq[lst[i]] = freq.get(lst[i], 0) + 1
print(freq)
"""

"""
quiz: separate out the unique and duplicated element from a list

lst = [4, 2, 7, 4, 9, 2, 4, 1, 7, 4, 2]
unique_lst = list()
duplicated_lst = list()
freq = {}
for i in range(len(lst)):
    if lst[i] in freq:
        freq[lst[i]] += 1
    else:
        freq[lst[i]] = 1

for key, val in freq.items():
    if val < 2:
        unique_lst.append(key)
    else:
        duplicated_lst.append(key)

print(unique_lst)
print(duplicated_lst)
"""

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

