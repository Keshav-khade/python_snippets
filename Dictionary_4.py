"""
# before starting exercise please do check this out.

LIST methods
.append(item) — mutates, returns None
python
lst = [1, 2, 3]
lst.append(4)
print(lst)          # [1, 2, 3, 4]
# NEVER do: lst = lst.append(4)  -> lst becomes None

Adds a single item to the end of the list, in place.

.extend(iterable) — mutates, returns None
python
lst = [1, 2, 3]
lst.extend([4, 5])
print(lst)          # [1, 2, 3, 4, 5]
# NEVER do: lst = lst.extend([4,5]) -> lst becomes None

Adds all elements of another iterable to the end, in place. (Compare: .append([4,5]) would add the whole list as one item → [1,2,3,[4,5]] — a common mix-up with .extend().)

.sort() — mutates, returns None
python
lst = [3, 1, 2]
lst.sort()
print(lst)          # [1, 2, 3]
# NEVER do: lst = lst.sort() -> lst becomes None

lst.sort(reverse=True)
print(lst)          # [3, 2, 1]

Sorts the list in place, ascending by default.

sorted(iterable) — does NOT mutate, returns a NEW list
python
lst = [3, 1, 2]
new_lst = sorted(lst)
print(new_lst)      # [1, 2, 3]
print(lst)           # [3, 1, 2]  <- original unchanged!

This is the opposite pattern of .sort() — it's a built-in function (not a method), and it's safe/required to assign since it returns a brand new sorted list instead of modifying the original.

DICT methods
.get(key, default=None) — does NOT mutate, returns a value (safe to assign)
python
d = {"a": 1}
val = d.get("a")          # 1
val2 = d.get("z", "N/A")  # "N/A", key not added to d
print(d)                    # {"a": 1}  <- unchanged

Just reads a value safely. Never modifies the dict, even if the key is missing.

.setdefault(key, default) — mutates (conditionally) AND returns a value
python
d = {"a": 1}
val = d.setdefault("a", 99)   # "a" exists -> returns 1, dict UNCHANGED
print(val, d)                   # 1 {'a': 1}

val2 = d.setdefault("b", 99)  # "b" missing -> CREATES d["b"]=99, returns 99
print(val2, d)                  # 99 {'a': 1, 'b': 99}

This is the odd one out — it's the only method here that both mutates (only when the key is missing) and safely returns something useful (the actual value now in the dict) — which is exactly why it fixed our .append() bug: result.setdefault("even", []).append(num) gets you the real list living inside the dict, ready to .append() onto directly.

.update(other_dict) — mutates, returns None
python
d = {"a": 1, "b": 2}
d.update({"b": 20, "c": 3})
print(d)             # {'a': 1, 'b': 20, 'c': 3}
# NEVER do: d = d.update(...) -> d becomes None

Merges another dict's key-value pairs into this one, in place. Overlapping keys get overwritten.

.pop(key, default) — mutates, returns the REMOVED VALUE (safe to assign — this is the point of using it)
python
d = {"a": 1, "b": 2}
val = d.pop("a")
print(val, d)          # 1 {'b': 2}

val2 = d.pop("z", "not found")
print(val2)             # "not found"  -> no crash

Removes the key and gives you back its value in one step — this is exactly why .pop() is safe/useful to assign, unlike .append().

.popitem() — mutates, returns a tuple (key, value) of the last inserted item
python
d = {"a": 1, "b": 2, "c": 3}
item = d.popitem()
print(item, d)          # ('c', 3) {'a': 1, 'b': 2}

Removes and returns the most recently added key-value pair as a tuple (since Python 3.7+ dicts preserve insertion order). No arguments — you can't pick which key to pop, unlike .pop(key).
"""

"""
Section D: Dictionaries + Other Data Structures (25–29)

1.Given a list of dictionaries (like DB rows): [{"id":1,"name":"A"},{"id":2,"name":"B"}], convert it into a single dictionary keyed by id. ⭐⭐⭐

2.Group a list of numbers into even/odd using a dictionary: {"even": [...], "odd": [...]}.

3.Given a list of transactions [{"user":"A","amount":100}, {"user":"B","amount":200}, {"user":"A","amount":50}], compute total amount per user using a dictionary.

4.Implement a simple LRU cache behavior check — use a dictionary + list to track insertion order and evict the oldest key when size exceeds a limit (no OrderedDict/functools).⭐⭐⭐

5.Find the intersection of keys between two dictionaries, and separately, the intersection of key-value pairs that match exactly in both.

"""
"""
problem statement: we have give a list of dictionary suppose list of employee details and all. Suppose if we have to find someone with their id we have to traver on entire list which end up taking o(n) time but if we can build a nested dictionaries with their id problem cuts down to only o(1) time that where by just know someones id will give us a complete description about them. (dictionaries uses hashmap for faster lookups)
q1.
lst = [{"id":1,"name":"A"},{"id":2,"name":"B"}]

# # using generic structure
result = dict()
for temp_d in lst:
    result[temp_d["id"]] = temp_d
print(result)

# # using dictionary comprehension
result = {temp_d["id"]:temp_d for temp_d in lst}
print(result)

# same idea needing o(n) complexity
for row in lst:
    row_copy = row.copy()
    row_id = row_copy.pop("id",None)
    result[row_id] = row_copy
print(result) # too clean and clear approach

ex.2
employees = [
    {"id": 101, "name": "Amit", "dept": "Backend"},
    {"id": 102, "name": "Sara", "dept": "Frontend"},
    {"id": 103, "name": "Karan", "dept": "Backend"}
]
result = dict()
for row in employees:
    row_copy = row.copy()
    row_id = row_copy.pop("id",None)
    result[row_id] = row_copy

print(result)
"""

"""
q2.
def dict_builder(lst):
    result = dict()
    for num in lst:
        if num%2 == 0:
            result.setdefault("even",[]).append(num)
        else:
            result.setdefault("odd",[]).append(num)
    return result

lst_of_num = [1,2,3,4,5,6,7,8,9,10]
res_dict = dict_builder(lst_of_num)
print(res_dict)

# same program with different approach
def dict_builder(lst):
    result = dict()
    for num in lst:
        key = "even" if num % 2 == 0 else "odd"
        if key not in result:
            result[key] = []
        result[key].append(num)
    return result
"""

"""
q3.
lst = [{"user": "A", "amount": 100}, {"user": "B", "amount": 200}, {"user": "A", "amount": 50}]
major_dict = dict()

for d in lst:
    if d["user"] in major_dict:
        major_dict[d["user"]]["amount"] += d["amount"]
    else:
        new_key = d.pop("user",None)
        major_dict[new_key] = d

user = input("enter user name: ").upper()
val = major_dict.get(user,{}).get("amount","N/A")
print(val)

"""

"""
# q4. LRU_Cache please chech out 
import LRU_Cache_base
import LRU_Cache_major
"""

"""
q5.
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 2, "c": 99, "d": 4}

ex.1
# problem takes o(n^2)
result = set()
for key,val in d1.items():
    for key1,val1 in d2.items():
        if key == key1:
            result.add(key)
print(result)

ex.2
common_keys = d1.keys() & d2.keys()
print(common_keys)   # {'b', 'c'}

ex.3
# complexity o(n)
unique = set()
for key in d1.keys():
    if key in d2:
        unique.add(key)
print(unique)

ex.4
# unique_pair with exactly matching key value pairs = {}
for key in d1.keys():
    if key in d2 and d2[key] == d1[key]:
        unique_pair[key] = d1[key]
print(unique_pair)

# by using direct method with & and items()
intersection = d1.items() & d2.items()
print(type(intersection))
print(dict(intersection))

Why does & work on .keys()? dict.keys() returns a special "view" object that supports set-like operations (& = intersection, | = union, - = difference) directly — because dictionary keys are inherently unique, just like set elements. You could also write it more explicitly:

common_keys = set(d1.keys()) & set(d2.keys())

Both give the same result — the .keys() version is just slightly more idiomatic since it skips an unnecessary set() conversion.
"""




