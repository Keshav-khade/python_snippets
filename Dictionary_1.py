"""
1. stores data in key value pairs.
2. python stores dictionaries internally as hash tables
d ----> [dict object]
           |
           entries array:
           [ (h1, ptr --> "name" (heap str obj), ptr --> "Rahul" (heap str obj)),
             (h2, ptr --> "age"  (heap str obj), ptr --> 27      (heap int obj)) ]

3. it's mutable data structure.
4. you can't have indexing and slicing on it.
5. average lookup time o(1)
6. insertion order preserved.
"""
"""
q1. Create a dictionary of 5 students with roll numbers as keys and names as values. Print all names.

stu_dct = dict()
stu_dct["roll_1"] = "keshav"
stu_dct["roll_2"] = "monu"
stu_dct["roll_3"] = "Rahul"
stu_dct["roll_4"] = "Raj"
stu_dct["roll_5"] = "kartik"

print(stu_dct)

for val in stu_dct.values():
    print(val)
    
ex.2
students = {
    101: "Ravi",
    102: "Sita",
    103: "Amit",
    104: "Neha",
    105: "Karan"
}
for roll, name in students.items():
    print(name)

# or simply:
print(list(students.values()))
"""

"""
q2. Add a new student to the dictionary from Q1 without overwriting existing ones.
stu_dct = dict()
stu_dct["roll_1"] = "keshav"
stu_dct["roll_2"] = "monu"
stu_dct["roll_3"] = "Rahul"
stu_dct["roll_4"] = "Raj"
stu_dct["roll_5"] = "kartik"

print(stu_dct)

for val in stu_dct.values():
    print(val)

# adding new student to dict
stu_dct["roll_6"] = "Ram"

print(stu_dct)
"""

"""
3. Given d = {"a": 1, "b": 2, "c": 3}, update value of "b" to 20 and add a new key "d": 4 in a single update() call.

# update the diction in generic way
d = {"a": 1, "b": 2, "c": 3}
# updating existing values
d["b"] = 20
print("after updated: ",d)
d["d"] = 4
print("after insertion",d)

# updating diction using single update call
d = {"a": 1, "b": 2, "c": 3}
# update b value and add new value to dictionary
d.update({"b":20,"d":4})
print(d)
"""

"""
q4. Remove a key from a dictionary two ways: using pop() and using del. Show the difference in behavior when the key doesn't exist.
d = {"a": 1, "b": 2, "c": 3}

# using del
del d["c"]
print("after deleting c: ",d)

# When key doesn't exist
try:
    del d["d"] # keyError
except KeyError as e:
    print("Error: ",e)

# using pop()
d.pop("a")
print("after deleting a: ",d)

# When key doesn't exist
try:
    res = d.pop("c") # keyError
    print("after deleting c: ",res)
except KeyError:
    print("Error keyError found")

try:
    res = d.pop("c") # keyError
    print("after deleting c: ",res)
except KeyError as e:
    print("Error keyError found",e)
    
d = {"a": 1, "b": 2}

# pop() - can provide a default, won't crash if key missing
val = d.pop("a")
print(val)          # 1
val2 = d.pop("x", "not found")
print(val2)         # "not found" -> no error

# del - raises KeyError if key doesn't exist, no return value
del d["b"]
print(d)
try:
    del d["x"]
except KeyError:
    print("KeyError: key not found")
"""

"""
d = {"a": 1, "b": 2, "c": 3}
# after deleting specific key with pop you will get back it's corresponded deleting value
res = d.pop("a")
print("after deleting d: ",res)

# if you don't handle by default None with pop it will raise KeyError
res = d.pop("d")
print("after deleting d: ",res)

# you can handle KeyError by writing None as Default
res = d.pop("d",None)
print("after deleting d: ",res)
"""

"""
Given d = {"x": 10, "y": 20, "z": 30}, write code to safely fetch a key "w" that doesn't exist, returning -1 as default, without using try/except.

d = {"x": 10, "y": 20, "z": 30}
fe_val = d.get("w",-1) # syntax: get(self,key,default)
print(fe_val)
"""

"""
question.5 how to fetch key : value pairs from the dictionary

d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}

# keys only
print(d1.keys(), end=' ')
print(d1.values())

# values only
print(d2.keys(), end=' ')
print(d2.values())

# keys only and with type casting
res = list(d1.values())
print(type(res),"\t",res)
"""

"""
6. Merge two dictionaries d1 = {"a": 1, "b": 2} and d2 = {"b": 20, "c": 3} such that d2's values override d1's on conflict. Show 2 different ways to do this (one must use | operator).

d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}

# update mergers two dictionaries using update()
d1.update(d2)
print(d1)

# merge two dictionaries using |, this used to perform union in sets
d1 = d1 | d2
print(d1)
"""

"""
7. Check if a key exists in a dictionary — write it two ways (in keyword and .get()).

d = {"x": 10, "y": 20, "z": 30}

# first ways of finding key using in membership operator
if "x" in d:
    print("x is in dict")

# second way of finding key using .get()
res = d.get("f","key not found")
print(res)
"""

"""
8. Given a dictionary of items and prices, find the item with the maximum price using max() with a key function (no manual loop).

ex.1
# using very brute force o(n)
max_price = 0
pro_name = ""
for key, value in pro_list.items():
    if value > max_price:
        max_price = value
        pro_name = key
print(f"max_price: {max_price}, pro_name: {pro_name}")

ex.2
# using max() / min()
pro_list = {"item1":20, "item2":30, "item3":40, "item4":50, "item5":60, "item6":70, "item7":80}

# minimum value
res = min(pro_list.values())
print(res)
# maximum value
res = max(pro_list.values())
print(res)

"""

"""
keyword arguments -> **dict

ex.1
Unpacking dict values
d1 = {"a": 1, "b": 2}
res = {**d1}      # valid - creates a new dict, a copy of d1
print(res)        # {'a': 1, 'b': 2}

ex.2
def show(a, b):
    print(a, b)
show(**d1)   # equivalent to show(a=1, b=2)

d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}
merged = {**d1, **d2} # it will like python spreading one diction first and then second and so on

res = {**d1} to make a shallow copy of a single dict
(same effect as d1.copy())
"""

"""
prices = {"apple": 50, "banana": 20, "mango": 80, "grapes": 60}

# by default if obj is given it will iterate over it's keys
for val in prices:
    print(val)

# prices = {"apple": 50, "banana": 20, "mango": 40, "grapes": 60}
# So max(prices) alone would just compare the keys as strings alphabetically — not what we want.
res = max(prices)
print(res)

# this only give you value not key
max(prices.values())   # returns 80

# if you want key as well as it's value you lambda expression
# For each key `x` in prices, compute prices.get(x), then find the x with the max result
res = max(prices, key=lambda x: prices.get(x))
print(type(res))
print(res,":",prices[res])

# # same logic using tuples .items gives you key value pairs as tuple
res = max(prices.items(), key=lambda item: item[1])
print(type(res))
print(res)

# ultimately in a single traversal
res = max(prices, key=prices.get)
print(res, prices[res])
"""

"""
q1. how to count frequency of element without using dictionary

lst = [2,3,4,5,2,3,2]
for i in range(len(lst)):
    cou = 0
    k = 0 # this k is for is_seen if it's seen earlier don't print
    for j in range(len(lst)):
        if lst[i] == lst[j]:
            cou += 1
            if j < i:
                k += 1
                break
    if k==0:
        print(f"count for {lst[i]} is {cou}")
"""
