# these are the advance list concepts that you should know

# reverse the list takes O(n^2)
lst = [10,20,30,40,50]
rev =[]
for item in lst:
    rev = [item] + rev
print(rev)

#concatinate the list
lst1 = ['a','b','c']
lst2 = ['A','B','C']
lst3 = lst1 + lst2
print(lst3)

# reverses the list in-place
lst = [10,20,30,40,50]
lst.reverse()
print(lst)

# using list slicing
lst = [10,20,30,40,50]
lst = lst[::-1]
print(lst)

# removing the duplicate values from the list
lst = [10,20,30,40,50,10,20,30,40]
fine_lst = []
for item in lst:
    if item not in fine_lst:
        fine_lst.append(item)
print(fine_lst)

# rotate a list by k position to right
lst = [1,2,3,4,5]
n = len(lst) # length of string
k = 7 # positions forward
# k = k%n Modulus reduces unnecessary full cycles
lst = lst[-k:] + lst[:-k]
print(lst)

# flatten a nested list
lst = [[1,2],[3,4],[5,6]]
lst1 = []
for item in lst:
    for sub in item:
        lst1.append(sub)
print(lst1)
        
# print the first and second largest elments time/space o(n) o(1)
lst = [10, 5, 20, 8, 20]
first = second = float('-inf') #generates negative integer which is too smallest
"time complexity is o(n)"
for num in lst:
    if num > first:
        second = first 
        first = num
    elif num > second and num != first:
        second = num
print(first, second)

# we can do it in another way also o(nlogn) + o(n)
lst1 = [10, 5, 20, 8, 20]
lst1 = list(set(lst1))
lst1.sort(reverse = True)
print(lst1)
print(lst1[0],lst1[1])

# we can also take help of heapq good for large data fast and clean time/space o(n)
import heapq
lst = [10, 5, 20, 8, 20]
largest_two = heapq.nlargest(2, set(lst))
print(largest_two[0], largest_two[1])

# if all the element are same so how you can find second largest
lst = [5, 5, 5]
if len(set(lst)) < 2:
    print("there is no second element exists")

# list is palindrome or not
seq = [1,2,3,2,1]
is_pal = True
for i in range(len(seq)//2):
    if seq[i] != seq[-(i+1)]:
        is_pal = False
print(is_pal)

# list comprehension and regular looping
square = []
for x in range(5):
    square.append(x**2)
print(square)

# another way to do this
square = [x**2 for x in range(5)]
print(square)

# multiply and same logic for another operators
lst = [1,5,4,6,7,3,2]
result = [i*2 for i in lst if i > 3]
print(result)

# formating the list values
prices = [100,250,345,450]
result = [format(p*1.1,".2f") for p in prices]
print("updated_prices: ",result)

# If the digit after rounding is exactly 5, Python rounds to the nearest EVEN number ,banker's rounding
prices = [100,250,345,450]
result = [round(p*1.1,3) for p in prices]
print("updated_prices: ",result)

prices = [99.99, 149.95, 249.5]
updated = [round(p * 1.18, 2) for p in prices]
print(updated)

# difference between round() and formatting 
value = 3.5
print(round(value, 2))
print(f"{value:.2f}")


# formatting using f-strings
prices = [10, 20, 30]
formatted = [f"₹{p*1.075:.2f}" for p in prices]
print(formatted)

"""
things to remember
<5 → round down
>5 → round up
==5 → round to nearest EVEN number
"""

# names less than 3 words means short-names will be excluded
names = ["ali","ravi","jo","kartik"]
filtered = [n for n in names if len(n) > 3]
print(filtered)

# email validation
emails = ["kartik@gamil.com","monu@gamil.com","maagamil.com","papa.gamil.com"]
correct = [e for e in emails if "@" in e]
print(correct)

# apply prefix to generate id's
nums = [64,65,70,66]
id = ["DS0"+ str(n) for n in nums]
print(id)

# count survey data
survey = ["yes", "no", "yes", "NO", "Yes", "YES"]
true_list  = [v for v in survey if v.lower() == "yes"]
false_list = [v for v in survey if v.lower() != "yes"]
print("True:", true_list)
print("False:", false_list)

# other way to do this
survey = ["yes", "no", "yes", "NO", "Yes", "YES"]
classified = ["true" if v.lower() == "yes" else "false" for v in survey]
print(classified)

# some list function and methods that we can use in our day to day tasks
lst = [12,13,14,15]
a = max(lst)
print(a)

lst = [12,13,14,15]
a = min(lst)
b = len(lst)
print(a)
print("length of this string is: ",b)

lst = [4,2,3,1,5]
new_lst = sorted(lst)
print(new_lst)

str1 = "banglore"
lst = list(str1)
print(lst)

lst2 = [7,5,6,3,2,2]
lst2.append(5)
print(lst2)

lst2 = [7,5,6,3,2,2]
lst2.insert(2,7)
print(lst2)

lst1 = [1,2,3]
lst2 = [4,5]
lst1.extend(lst2)
print(lst1,lst2)

lst2 = [7,5,6,3,2,2]
lst2.remove(2)
print(lst2)

lst2 = [7,5,6,3,2,2]
a = lst2.pop()
print(a)
print(lst2)

lst2 = [7,5,6,3,2,2]
lst2.reverse()
print(lst2)

lst2 = [7,5,6,3,2,2]
lst2.sort()
print(lst2)

lst2 = [7,5,6,3,2,2]
lst2.clear()
print(lst2)

# add item to the grocery list
lst = ["potato","tomoto","coliflower","chilli"]
lst.append("sugar")
lst.sort()
lst.remove("coliflower")
print(lst)

# average max min of the students score
scores = [78,98,85,76,92,90,87]
avg = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)
print("average:{} , Highest:{} , Lowest:{}".format(avg,highest,lowest))

# count the particular itme
lst = ["apple","banana","mango","apple","orange"]
times = lst.count("apple")
print("count of your item is: ",times)

"responses".count("e")