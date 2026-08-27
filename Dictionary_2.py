"""
Section B: Iteration & Transformation (9–16)

1.Given marks = {"Ravi": 85, "Sita": 90, "Amit": 70}, print only students who scored above 75.
2. Swap keys and values of a dictionary: {"a": 1, "b": 2} → {1: "a", 2: "b"}.
3.Given a list of words, build a dictionary of word → length using a dictionary comprehension.
4. Count the frequency of each character in a string using a dictionary (no Counter).
5. Given d = {"a": 1, "b": 2, "c": 3}, create a new dict with only keys "a" and "c" using dict comprehension.
6. Sort a dictionary by its values in descending order and print as a list of tuples.
7. Given two lists keys = ["a","b","c"] and values = [1,2,3], build a dictionary using zip().
8. Invert a dictionary where values might repeat (e.g., {"a":1,"b":1,"c":2}) — group keys with the same value into a list under that value.

"""
"""
1. 
marks = {"Ravi": 85, "Sita": 90, "Amit": 70}
for name, score in marks.items():
    if score > 75:
        print(name, score)

# or as a dict comprehension if you want the filtered dict itself:
top_students = {name: score for name, score in marks.items() if score > 75}
print(top_students)   # {'Ravi': 85, 'Sita': 90}
"""

"""
Note : The rule to remember 🧠
1. Don't change the size of a dictionary while iterating over that same dictionary.

2. 
TypeError: 'dict_values' object is not subscriptable

d = {"a": 1, "b": 2}
new_d = dict()
# this operation gives you dict_item object which is not subscriptable but iterable
res = d.items() # inside this dict_item object there are list of tuple you unpack these tuples 

for pairs in d.items():
    new_d[pairs[1]] = pairs[0]
print(d)
# here you have swaped item in new dictionary
print(new_d)

d = {"a": 1, "b": 2}
swapped = {value: key for key, value in d.items()}
print(swapped)   # {1: 'a', 2: 'b'}
"""

"""
q3. 
word_lst = ["boys","cars","toys","bottle","chair","table","bed","malicious","suspicious","random"]
d = dict()

ex.1 Manual looping
for word in word_lst:
    if len(word) > 0:
        # if any word is duplicated it will override that word
        d[word] = len(word)
print(d)

ex.2 using dictionary comprehension
word_lst = ["boys","cars","toys","bottle","chair","table","bed","malicious","suspicious","random"]
d = dict()
# dictionary comprehension
d = {word: len(word) for word in word_lst if len(word) > 0}
print(d)

answer: 
words = ["apple", "banana", "kiwi", "fig"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)   # {'apple': 5, 'banana': 6, 'kiwi': 4, 'fig': 3}
"""

"""
q4.
Str = "The world is around the beautiful sea"
lst = Str.split()
Str = "".join(lst).lower()
d = dict()
for char in Str:
    d[char] = d.get(char,0) + 1  
print(d)

# using manual looping
s = "hello world"
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)

# More Pythonic version using dict.get():
freq2 = {}
for ch in s:
    freq2[ch] = freq2.get(ch, 0) + 1
print(freq2)
"""

"""
q5.
d = {"a": 1, "b": 2, "c": 3}
d = {key:val for key,val in d.items() if key != "b"}
print(d)

d = {"a": 1, "b": 2, "c": 3}
wanted_keys = {"a", "c"}
new_d = {k: v for k, v in d.items() if k in wanted_keys}
print(new_d)   # {'a': 1, 'c': 3}
"""

"""
q6.
Note: 
sorted() here works exactly like max() did earlier — key=lambda item: item[1] tells it to sort based on each tuple's second element (the value), not the tuple itself.

pro_price = {
    "table" : 120,
    "bottle": 70,
    "chair": 70,
    "watch" : 100,
    "mobile": 80,
    "wallet": 60,
    "mouse": 40
}

p = sorted(pro_price.items(), key=lambda tup: tup[1], reverse = True)
print(p)

"""

"""
q7.
zip() ->
 zip(*iterables, strict=False)
 |
 |  The zip object yields n-length tuples, where n is the number of
 |  iterables passed as positional arguments to zip().  The i-th element
 |  in every tuple comes from the i-th iterable argument to zip().  This
 |  continues until the shortest argument is exhausted.
 |
 |  If strict is true and one of the arguments is exhausted before the
 |  others, raise a ValueError.
 |  it requires type casting function to make a relevant pair.
 |
 |     >>> list(zip('abcdefg', range(3), range(4)))
 |     [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]

keys = ["a","b","c"]
values = [1,2,3]

new_d = dict(zip(keys, values,strict=False))
print(new_d)
"""

"""
q8.
Note:
setdefault(value, []) means: "if value isn't a key yet, create it with an empty list; either way, return that list" — so you can immediately .append() to it in one line instead of the if/else check.

 
d = {"a": 1, "b": 1, "c": 2}
inverted_1 = {}
# using basic logic
for key,val in d.items():
    if val not in inverted_1:
        inverted_1[val] = []
    inverted_1[val].append(key)

inverted_2 = {}
# using setdefault()
for key, val in d.items():
    inverted_2.setdefault(val, []).append(key)

print("This is dictionary_1 ->",inverted_1)
print("This is dictionary_2 ->",inverted_2)
"""
