									# python little snippet
"""
for i in range(3):
    sum =0
    if i == 1:
        sum = sum + i
print(sum)
    

									# ATM login with max attempts

correct_pin = "1234"
for attempts in range(3):
    pin = input("Enter your pin sir: ")
    if pin == correct_pin:
        print("access granted")
        break
    print("wrong password try again sir !")
else:
    print("Your account is blocked: ")


									# Filter out invalid scores 

scores = [12,34,-9,67,-15,7,-54]
for i in scores:
    if i < 0:
        continue
    print(i)

									# stop once correct item is found in inventory

inventory = ["pen","Bottle","books","copy","watch","eraser","lunch box"]
item_ = "books"

for item in inventory:
    if item == item_:
        print(f"{item_}: is found in inventory")
        break

"""
# .split() method use cases
s = "ajay,kumar,singh"
s1 = s.split(",")
print(type(s1))

# you can also have default split()
line = "Data analysis with Python"
s2 =line.split()

# split using a custom delimeter
date = "2026-02-05"
d1 = date.split("-")
print(d1)

# real-scenarios , used-in real world scenarios like API Respones , raw text files , logs , while reading csv documents and raw data
log = "101,John,Sales,45000"
l1 = log.split(",")
print(l1)

# extract domain name from emails
# customer analysis /  email classification / fraud detection
email = "john.doe@gmail.com"
email = email.split("@")[1]
print(email)

# split product codes when it used
product = "ELEC-TV-2025"
category,item,year=product.split("-")
print(category,"\n",item,"\n",year)

"""
syntax -> separator.join(iterable)
.join() method putting values back together based on your separator

"""

# small snippets
chars = ['a', 'j', 'a', 'y']
chars = "".join(chars)
print(chars)

# another example
words = ['Data', 'Analysis', 'Python']
words = " ".join(words)
print(words)

# real data cleaning scenarios , here remove extra space how?
name = "  John   Doe  "
name = " ".join(name.split())
print(name)

# Create CSV row from list
# ✔️ Used when: / exporting cleaned data / writing to files
row = ['101', 'John', 'Sales', '45000']
'use minimum variable as possible because of memory issue try to override the variables when must'
row = ",".join(row)
print(row)

# Standardize phone numbers
phone = "123-456-7890"
# phone = "".join(phone.replace("-",''))
phone = "".join(phone.split("-")) # this is the efficient way of doing this work
print(phone)

# ✔️ Used in: customer databases / validation pipelines
text = "Python@is#awesome!"
# clean = "".join(text.split("@"))
# clean = "".join(clean.split("#"))

cleaned = "".join(ch for ch in text if ch.isalnum()) # optimal method for cleaning
print(cleaned)

# ❌ Slow
result = ""
for ch in ['a', 'j', 'a', 'y']:
    result += ch
print(result)

# use join method instead of this
lst = ['a', 'j', 'a', 'y']
lst = "".join(lst)
print(lst) # fast and efficient


# some practice questions
#1️⃣ Extract year from date
date = "2025/12/26"
ex_year = date.split("/")[0]
print(ex_year)

# 2️⃣ Clean this messy sentence
text = "  Python   is    powerful  "
cleaned = ' '.join(text.split())
print(cleaned)

# 3️⃣ Convert this to email format
# answer -> “I’d split the name into parts, normalize it, then join with a delimiter.”
name = "john doe"
# Expected → john.doe@gmail.com
email = ".".join(name.split()) + "@gmail.com"
print(email)

# hide the middle name
name = "kartik ratnakar khade"
part = name.split() # now this is a list object
part[1] = "*" * len(part[1])
masked_name = " ".join(part)
print(masked_name)

"""
# check given string is palindrome
def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False
text = input("enter a text: ")
print(palindrome(text))

# another way to do this 
text = input("enter a text:")
palindrom = text == text[::-1]
print(palindrom)

"""

# extract the last word of a sentence
text = "I live in madhaya pradesh which is the heart of india"
last_word = text.split()[-1]
print(last_word)

# another way to do this
last_word = text.strip().split()[-1]
"""
text.strip().split()[-1]
✔️ Removes leading/trailing junk
✔️ Guarantees clean splitting
✔️ Best practice in data cleaning

strip()	    both ends
lstrip()	left only
rstrip()	right only


last_word = text.strip().split()[-1]
✔️ Handles:
    file input
    scraped text
    user input
    API responses
✔️ Production-ready code
"""
print(last_word)

"""
👉 split() without arguments

text.split()

DOES NOT split on single spaces " "
Instead, it splits on any whitespace and:

✅ Automatically ignores

leading spaces
trailing spaces
multiple spaces
"""

# finding a word greater than 5 characters
text = "AI is revolutionizing every industry across the world"
part = text.split()
f_long = next((word for word in part if len(word)>5),"not found")
print(f_long)


# logs analysis
# 🧪 Scenario 3: First keyword in text
keywords = ["error", "failed", "timeout"]
log = "request timeout after 30 seconds"
found = next((k for k in keywords if k in log), None)
print(found)

# stop immediately when you catch first even number
nums = [1, 3, 5, 5, 4]
even = next((i for i in nums if i%2==0),-1)
print(even)

# extract every second element from the string
text = "trees are play very crucial role in nature"
words = text.split()
s_words = words[::2]
print(" ".join(s_words))

# count the vowels in a sentences
text = "I love to study python"
count = 0
vowel = "aeiou"
for char in text:
    if char.lower() in vowel:
        count += 1
print("total number of vowel is:{}".format(count))

# mask any string with any given position
ifsc = "MAHABANK0883"
length = len(ifsc)
mask = ""
for i in range(length):
    if i < length-4:
        mask += "*"
    else:
        mask += ifsc[i]
print(mask)    

# removing all the duplicate characters , using this when order is important
text = "mississippi"
result = ""
for char in text:
    if char not in result:
        result += char
print("without duplicate:{}".format(result))

# you can remove duplicate using set method also
text1 = "mississippi"
set1 = set(text1)
print(set1)

# if you want a counter with characters than you should use counter
from collections import Counter
s = "mississippi"
g = Counter(s)
print(g)

# capitalize the first letter of each sentence
sentence = "python is great.coding is simple"
lst = sentence.split(".")
lst1 = []
for i in lst:
    lst1.append(i.strip().capitalize())
print(lst1)

# count the number of digits in a string
my_phone = "6265289405"
counter = 0
for i in my_phone:
    counter += 1
print(counter)
print(len(my_phone))

# convert snake case to title case
snake = "python_programming_language"
lst = snake.split("_")
lst1 = []
for i in lst:
    lst1.append(i.strip().capitalize())
lst1 = "_".join(lst1)
print(lst1)

# check if a string is strong password or not
password = input("Enter your password: ")

special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

if len(password) < 8:
    print("❌ Weak password: Minimum length should be 8")

elif not any(ch.isupper() for ch in password):
    print("❌ Weak password: At least one uppercase letter required")

elif not any(ch.islower() for ch in password):
    print("❌ Weak password: At least one lowercase letter required")

elif not any(ch.isdigit() for ch in password):
    print("❌ Weak password: At least one digit required")

elif not any(ch in special_chars for ch in password):
    print("❌ Weak password: At least one special character required")

else:
    print("✅ Strong password!")


# find and replace words without using .replace()
text = "Python is fun. Python is powerful and Python is easy."

replacements = {
    "Python": "Java",
    "fun.": "awesome."
}

words = text.split()
result = []

for word in words:
    if word in replacements:
        result.append(replacements[word])
    else:
        result.append(word)

final_text = " ".join(result)
print(final_text)
# replace "data" word with "info" all occurences
