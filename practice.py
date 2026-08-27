"""
Hackerrank
There are 5 students in this class whose names and grades are assembled to build the following list:
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade 37.2 of  belongs to Tina. The second lowest grade of 37.21  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.


students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
lst = []
# this is called list comprehension and unpacking.
for name, grade in students:
    lst.append(grade)
# for removing duplicates and gain a sorted list
s = list(set(lst))
# sort the list to get the second smallest value
s.sort()
# fetch the second smallest
sec_small = s[1]
lst = []
# traverse the nested list and get the name and sort them
for name, grade in students:
    if grade == sec_small:
        lst.append(name)
# sort the list to get the in place sort
lst.sort()

"""

"""
Problem: Word Frequency Counter

sentence = "the quick brown fox jumps over the lazy dog the fox runs"
lst = sentence.split()

freq = {}

for word in lst:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# one liner approach for above logic
for word in lst:
    freq[word] = freq.get(word,0) + 1

print(freq)
"""

"""
# find the duplicate element in the list

nums = [4, 5, 6, 7, 4, 8, 5, 9, 10, 6]
unique_set = set()
duplicated = []
for val in nums:
    if val in unique_set:
        duplicated.append(val)
    else:
        unique_set.add(val)

print(duplicated)
"""

"""
names = ["Harry", "Berry", "Tina", "Akriti", "Harsh", "Ben", "Alex", "Tanya"]
ex1.
# lst = []
# for word in names:
#     for ch in word:
#         if ch in lst:
#             break
#         else:
#             lst.append(ch)
#             break
#
# freq = dict()
# for ch in lst:
#     temp = []
#     for ind in range(len(names)):
#         if names[ind][0] == ch:
#             temp.append(names[ind])
#     freq[ch] = temp
#
# print(freq)

ex.2
# another better approach to group the same first character out
freq = {}
for name in names:
    first_letter = name[0]
    if first_letter in freq:
        freq[first_letter].append(name)
    else:
        freq[first_letter] = [name]

print(freq)
"""


