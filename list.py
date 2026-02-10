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