"""
1. The sorted() function can use a lambda as a key for custom sorting:
2. sorted() function returns a new list.
3. syntax = sorted(iterater , key=None , reverse=None)
4. in place of key you can use lambda function and in-place of reverse you can use True or false as per you want acsending or descending values

5. sorted uses timsort as internal logic
   Stable ✅
   Adaptive ✅ (fast on partially sorted data)
   Hybrid of merge + insertion sort

"""

# small snippets for practice
#1
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
students1 = sorted(students,key=lambda x:x[1])
print(students1)

#2 sorting by the length
words = ["apple", "pie", "banana", "cherry"]
words1 = sorted(words,key=lambda x:len(x))
words1 = sorted(words,key=len)
print(words1)

#2.1 you can also write this functin like this
def word_length(word):
    print("called for: ",word)
    return len(word)

words1 = sorted(words, key=word_length)
print(words1)
#here sorted calls function every time for example

#3 you will see how sorted creates a new list
nums = [4, 1, 3, 2]
nums1 = sorted(nums)
print(nums) # here original list remains as it is, right
print(nums1)

nums.sort() # now by the help of sort() we can modify the original list in-place, right
print(nums)

#4 enumerate() = value + identity It lets you sort data without losing where it came from.
lst = [50, 20, 40]
lst1 = sorted(enumerate(lst), key=lambda x: x[1])
"""
here enumerate preserves the index where the element comes from right
so it helps a lot in data analysis.
internally is proveides the list of tuple as [(0,50),(1,20),(2,40)]
then this list provided to sorted then it sorts based on second element of tuple right.
"""
print(lst1)

# 4.1 same function 
scores = [88, 92, 75]
ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
"finds scores largest to lowest but how do i know that who scores what use enumerate to retain index"
print(ranked)

#5 multiple level of sorting
students = [
    ('John', 90, 21),
    ('Alice', 90, 19),
    ('Bob', 85, 20)
]
sorted(students, key=lambda x: (-x[1], x[2]))
# first sortes based on first index decsending order and then based on age ascending order

#6 inside string based on indexing and slicing
files = ['file1', 'file10', 'file2']
print(sorted(files)) # 
sorted1 = sorted(files,key=lambda x:int(x[4:]))
print(sorted1)

# 7 sort this dict out
sales = {'A': 300, 'B': 150, 'C': 500}
sales1 = sorted(sales.items(),key=lambda x:x[1],reverse=True)
print(sales1)

# 8 used in data analysis , find top selling products
top_products = sorted(
    sales.items(),
    key=lambda item: item[1],
    reverse=True
)
print(top_products)