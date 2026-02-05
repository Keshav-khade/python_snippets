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
