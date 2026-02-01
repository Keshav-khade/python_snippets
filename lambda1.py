"""
1. filter() -> Select only what you want
          The filter() function creates a list of items for which a function returns True:
2.        Keeps elements where condition is True
          Does NOT modify, only filters
3.        filter() never modifies data
          It only decides: keep or discard
4. syntax -> filter(function, iterable)

5. filter() function returns a tuple 
                  
"""
# filter out even or odd numbers manually 
lst = [1,2,3,4,5,6,7,8,9]
lst1 = []
def is_even(lst):
          for i in lst:
                  if i % 2 == 0:
                    lst1.append(i)  
is_even(lst)
print(lst1)

# filter out number using filter() function
def is_even(i):
       if i % 2 ==0:
          return True
       else:
          return False
lst1 = list(filter(is_even,lst))
print(lst1)   
 
# using lambda function
lst1 = list(filter(lambda x: (x%2==0),lst))
print(lst1)

# you can use map() + filter() combined methods
nums = [1, 2, 3, 4, 5, 6]
"first takes out even numbers and then square it out"
result = list(
    map(lambda x: x*x,
        filter(lambda x: x % 2 == 0, nums))
)
print(result)

#  filter out the thinking based on True or False                
lst = [1,2,3,4,5,6,7,8]
"filter out the number which is greater than 3"
lst1 = list(filter(lambda x: x>3 , lst))
print(lst1)

# if you want to sort based on only value you can skip function also by placing None in the place of funcion

data = [0, 1, "", "hello", [], [1, 2], None, True, False]
lst1 = list(filter(None,data)) # filters out data based on true or false
print(lst1)

# how it is working internally
result =[]
for item in data:
      if item:
          result.append(item)

# using lambda function
lst1 = list(filter(lambda x: x,data))
print(lst1)

# keep only positive numbers
nums = [-3, -1, 0, 2, 4, 5]
nums1 = list(filter(lambda x:x>=0 ,nums))
print(nums1)

# keep only truthy values
data = [0, 1, None, 3, 0, 5]
data1 = list(filter(lambda x:x,data))
print(data1)

# keep only even numbers
nums = [1, 2, 3, 4, 5, 6]
nums2 = list(filter(lambda x:x%2==0,nums))
print(nums2)

# filter string longer than 3 character
words = ["hi", "hello", "sun", "python", "AI"]
words1 = list(filter(lambda x: len(x)>=3 ,words))
print(words1)

# remove empty strings
texts = ["apple", "", "banana", "", "cherry"]
texts1 = list(filter(lambda x:x != "",texts))
cleaned = list(filter(None,texts))
print(texts1)
print(cleaned)

# filter the values which are greater than 50
marks = {"A": 80, "B": 45, "C": 60}
marks1 = dict(filter(lambda x:x[1]>50,marks.items()))
print(marks1)

# filter list of tuples
students = [("A", 55), ("B", 70), ("C", 40), ("D", 85)]
s1 = list(filter(lambda x:x[1]>50,students))
print(s1)

# filter data which have valid salary
# used in data cleaning methods
data = [
    {"name": "A", "salary": 0},
    {"name": "B", "salary": 5000},
    {"name": "C", "salary": None},
    {"name": "D", "salary": 8000}
]

data2 = list(filter(lambda x:x["salary"],data))
print(data2)

# you can use your custom functions also instead of using lambda and all.
def custom(x):
     if x > 5:
          return x
Data = [3,7,2,1,9,10,43,-7,8,-4,65,-34,23]
data3 = list(filter(custom,Data))
print(data3)


# here is simple test for you what will be the output of this logic
data = ["", "0", 0, 1, [], [0], None]
print(list(filter(None, data)))

# python internally does this
temp = filter(None, data)
result = []
for item in temp:
    if item:
        result.append(item)

print(result)