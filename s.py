# how to access strings in python
"""
# using for loop
s = input("Enter a string: ")
n = len(s)
for i in range(n):
    print(s[i], end=' ')
print()

# using while loop
ind = 0
while ind < n:
    print(s[ind], end=' ')
    ind = ind + 1
print()

# using without indexing
for ch in s:
    print(ch, end=' ')
print()

# how using negative indexing we will print from 0, n same effect
for i in range(-n, 0):
    print(s[i], end=' ')
print()

# using for loop indexing reverse the string
for i in range(n-1, -1, -1):
    print(s[i], end=' ')
print()

# using negative indexing
for i in range(-1, -n-1, -1):
    print(s[i], end=' ')
print()
"""

"""
s = "naresh technologies"
print(s[::-1])
print()
print(s[-5:-13:-1])
print()
print(s[-5::-1])
print()
print(s[::-3])
"""

"""
s = "   naresh technologies   "
s = s.strip()
print(s)

s = s.upper()
print(s)

s = s.lower()
print(s)

s = s.title()
print(s)

s = s.capitalize()
print(s)

s = s.swapcase()
print(s)

k = s.find('TECHNOLOGIES')
print(k)

print(type(s))

try:
    s = s.index('kar')
    print(s)
except Exception as e:
    print(f"your error is: ", e)
"""

"""
s = input("Enter a string: ")
if s.isascii():
    print('this is in a range of 0 to 255 all characters')
    if s.isalnum():
        print('string can be characters , digits or both')
        if s.isalpha():
            print('all are alphabets')
            if s.islower():
                print('all are lower alphabets')
            else:
                print('all are upper case alphabets')
        else:
            print('all are digits')
    else:
        if s.isspace():
            print('string contains all spaces')
        else:
            print('string contains all special characters')
else:
    print('string contains only unicode characters')
"""

"""
split() -> split(sep=none , maxsplit = -1) -1 means no limit for split , both are optional
        -> it separate a string on whitespaces (tab, spaces, newline)
        -> returns a list of strings

s = 'Hello world'
print(id(s))
new_str = s.split()
print(id(new_str))

s = "a,b,c"
print(s.split(","))
# ['a', 'b', 'c']

s = "   hello    world   "
print(s.split())
# ['hello', 'world']   -> extra spaces collapsed, edges trimmed

print(s.split(" "))
# ['', '', '', 'hello', '', '', '', 'world', '', '', '']

s = "one two three four"
print(s.split(" ", 1))
# ['one', 'two three four']

print(s.split(" ", 2))
# ['one', 'two', 'three four']

line = "name=John Doe=Engineer"
key, value = line.split("=", 1)
print(key, "->", value)
# name -> John Doe=Engineer

# rsplit() example
path = "a/b/c/d.txt"
print(path.rsplit("/", 1))
# ['a/b/c', 'd.txt']

# multi charactor separator
s = 'one::two::three'
lst = s.split('::', -1)
print(lst)

s = 'kartik,25,engineer,120000'
fields = s.split(',')
name, age, role, salary = fields
print(name)

text = "kartik is my best friend\nHis mom and dad are lovely couples\nHis sister is hardworking woman"
lines = text.split("\n")
print(lines)
# ['line1', 'line2', 'line3']


data = "1,2,3;4,5,6;7,8,9"
maj = data.split(';')
# print(maj)
minor = [row.split(',') for row in maj]
# print(minor)
for r in range(len(minor)):
    for c in range(len(minor[0])):
        minor[r][c] = int(minor[r][c])

print("changing string to integer value")
for r in range(len(minor)):
    for c in range(len(minor[0])):
        print(minor[r][c], end=' ')
    print()

# how to make multiple operations on a string
s = "  Alice:30 , Bob:25 , Carol:28  "
people = s.strip().split(",")
people = [p.strip() for p in people]
print(people)
# ['Alice:30', 'Bob:25', 'Carol:28']

result = {}
for p in people:
    name, age = p.split(":")
    result[name] = int(age)
print(result)
# {'Alice': 30, 'Bob': 25, 'Carol': 28}

"".split()        # []                  -> empty string, no args = empty list
"".split(",")     # ['']                -> empty string, with sep = list with one empty string
"a".split(",")    # ['a']               -> no separator found = whole string as one item
"a,,b".split(",") # ['a', '', 'b']      -> empty string between consecutive separators
",a,b,".split(",")# ['', 'a', 'b', '']  -> leading/trailing separators create empty strings
"""

"""
join ->  
1. separator.join(iterable)
2.  both are required 
3. separator by default whitespace
4. Returns: a single string.
5. every element in an iterable must be a string or you will get typeerror

lst = ['hello', 'world']
result = " ".join(lst)
print(type(result))
print(result)

letters = ["a", "b", "c"]
s = " ".join(letters)
print(s)

# This is actually the fastest way to concatenate many strings in Python
# Level 2 — Empty separator (concatenation)
python = ["p", "y", "t", "h", "o", "n"]
print("".join(python))
# python

# ⚠️ Remember this rule: everything inside the iterable passed to join() must be a str. No exceptions.
nums = [1, 2, 3]
s = " ".join(str(i) for i in nums)
print(s)


# Level 4 — split() then join() — the classic combo
pythons = "  hello    world  "
# This is a very common idiom for normalizing whitespace — split (which collapses all whitespace) then rejoin with single spaces.
pythons = pythons.split()
s = " ".join(pythons)
print(s)
print(type(s))

parts = ["2026", "07", "01"]
s = "-".join(parts)
print(s)

items = ["apple", "banana", "cherry"]
s = "->".join(items)
print(s)

# Level 6 — Joining with a generator (memory efficient)
pythonsquares = (str(n**2) for n in range(5))
print(type(pythonsquares))
print(", ".join(pythonsquares))
# 0, 1, 4, 9, 16
# Generators work directly — join() consumes them lazily, no need to build a list first.
"""

"""
working of map() -> map(function, iterable)
map is a lazy iterator object that applies a function on the item of an iterable one at a time.
it not return list or anything it will return map object

big_map = map(str, range(10_000_000)) -> this is very important it will save your memory space
big_list = [str(n) for n in range(10_000_000)] -> this will create list of 10 million item space inefficient

minor = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in minor:
    print(",".join(map(str, row)))
# 1,2,3
# 4,5,6
# 7,8,9

# 1,2,3;4,5,6;7,8,9
rows = [",".join(map(str, row)) for row in minor]
# print(rows)
full_string = ";".join(rows)
print(full_string)

d = {"Alice": 30, "Bob": 25, "Carol": 28}

pairs = [f"{key}:{value}" for key, value in d.items()]
# print(pairs)
full_string = ", ".join(pairs)
print(full_string)

header = ["Name", "Age", "Job"]
row1 = ["Alice", "30", "Engineer"]
row2 = ["Bob", "25", "Designer"]

print("| ".join(header))
print("_"*40)
print("| ".join(row1))
print("| ".join(row2))

# 10 . edge cases
"-".join([])          # ''          -> empty list = empty string
"-".join(["solo"])    # 'solo'      -> single item = no separator applied
"".join(["a", "", "b"]) # 'ab'      -> empty strings just vanish
",".join(("x", "y"))  # 'x,y'       -> tuples work too, not just lists
"""

