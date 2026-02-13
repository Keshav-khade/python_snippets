# python snippet
s ="hello world"
s = "H" + s[1:]
print(s) 

# email masked creation
email = "khadekartik834@gmail.com"

"index('value') strictely checks the sub-string and raises valueerror if not found"
"syntax -> index(value,start,end)"
"Can be one character or multiple characters"

pos = email.find("@")
if pos != -1:
    masked_email = email[0] + "*****" + email[pos:]
else:
    masked_email = "Invalid email"
print(masked_email)  


# validated a perticular file type
file = "report2025.pdf"
if file.endswith(".pdf"):
    print("valid file type")
else:
    print("file type is not valid")

"""
here .endswith() checks that string is endswith the substring or character or not
it return True and false value 
syntax -> .endswith("sub-str",start,end)
start specifies from where to start 
and end specifies where to end
"""

# message replacing method
message = "this product is awesome"
if "awesome" in message:
    new_message = message.replace("awesome","great")
    print(new_message)

"""
syntax of .replace() ->
.replace("old","new",count)
old -> old value
new -> new str
count -> how many time if value repeats change all of them
1. replace not changes the original strings it returns the new one
2. old and new string must needed you can't skip them
3. Maximum number of replacements
   Replaces from left to right
4. 
"""

# let's see some snippets
text = "hello world"
new_text = text.replace("world", "Python")

print(new_text)  # hello Python
print(text)      # hello world
print(id(text))
print(id(new_text))
# there id's also different

# string replacement along with count
text = "ha ha ha"
print(text.replace("ha", "ho",2))

#replace all occurances
text = "bad bad bad"
print(text.replace("bad", "good"))

#case sensitivity
s = "Awesome"
s = "Awesome".lower().replace("awesome", "great")  # No change
# s.lower().replace("Awesome","good")
print(s)

# chain replacement
text = "2025/02/03"
text = text.replace("/", "-")
print(text)
