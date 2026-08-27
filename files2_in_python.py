"""
                    working with os module and submodule path or you can say variable.


os.path.splitext(path) -> 
1. Split the pathname path into a pair (root, ext) such that root + ext == path, and the extension, ext, is empty or begins with a period and contains at most one period.
2. it returns a tuple object you have to unpack it for make use of it.

os.path.getsize(path) ->
Return the size, in bytes, of path. Raise OSError if the file does not exist or is inaccessible.

Absolute Path -> complete path of the file from drive to file
ex. c:\\c and cpp\\DSA_placement_series\\files2_in_python.py

relative path -> path from current working directory to file
ex. .\\DSA_placement_series\\files2_in_python.py

os.path.abspath(path) ->
Return a normalized absolutized version of the pathname path.
import os
path = os.path.abspath("demo.txt")
print(path)

os.path.exists(path) -> 
Return True if path refers to an existing path or an open file descriptor. Returns False for broken symbolic links.
ex. is_exists = os.path.exists("demo.txt")

time.ctime([secs]) -> ctime from time module in python
Convert a time expressed in seconds since the epoch to a string of a form: 'Sun Jun 20 23:21:05 1993' representing local time. The day field is two characters long and is space padded if the day is a single digit, e.g.: 'Wed Jun  9 04:26:40 1993'.

os.path.getmtime(path) -> 
Return the time of last modification of path. The return value is a floating-point number giving the number of seconds since the epoch (see the time module). Raise OSError if the file does not exist or is inaccessible.

os.path.getctime(path) -> 
Return the system's ctime which, on some systems (like Unix) is the time of the last metadata change, and, on others (like Windows), is the creation time for path. The return value is a number giving the number of seconds since the epoch (see the time module). Raise OSError if the file does not exist or is inaccessible.

-> difference between readlines() and splitlines()
with open("demo.txt","r") as f:
          content = f.readlines()
          print(content)
          content = "".join(content)
          print(content.splitlines())

splitlines() ->
In Python, the splitlines() method is used to split a string into a list of lines, breaking at line boundaries (\n, \r, or \r\n).
Syntax
          string.splitlines([keepends])
          keepends (optional, default=False):
                    False → Removes the newline characters from the result.
                    True → Keeps the newline characters at the end of each line.
"""

"""
                                        primary info of a file.
import os

filename = "demo.txt"

# 1. File ka naam aur extension alag karna
name, extension = os.path.splitext(filename)
print("File name:", name)
print("Extension:", extension)

# 2. File ka size (bytes mein)
size = os.path.getsize(filename)
print("File size (bytes):", size)

# 3. File ka full/absolute path
full_path = os.path.abspath(filename)
print("Absolute path:", full_path)

# 4. File exist karti hai ya nahi
print("File exists:", os.path.exists(filename))

# 5. Last modified time
import time
mod_time = os.path.getmtime(filename)
print("Last modified:", time.ctime(mod_time))

# 6. Creation time
create_time = os.path.getctime(filename)
print("Created on:", time.ctime(create_time))
                                        
                                        secondary info of a file:

with open("demo.txt", "r") as f:
          content = f.read()
          lines = content.splitlines()

# words in a string is
words = content.split()

vowels = "aeiouAEIOU"
vowel_cou = 0
consonant_cou = 0
digit_cou = 0
spaces_cou = 0
for ch in content:
          if ch.isalpha():
              if ch in vowels:
                    vowel_cou += 1
              else:
                    consonant_cou += 1
          elif ch.isdigit():
                 digit_cou += 1
          elif ch.isspace():
                 spaces_cou += 1

# --- Print all results ---
print("Character count:", len(content))
print("Line count:", len(lines))
print("Word count:", len(words))
print("Vowel count:", vowel_cou)
print("Consonant count:", consonant_cou)
print("Digit count:", digit_cou)
print("Space count:", spaces_cou)

"""

"""
# wap to input a source file and target file copy the content from source to target all in capital letters.

with open("demo.txt","r") as f1, open("demo1.txt", "w") as f2:
          content = f1.read()
          f2.write(content.upper())

f = open("demo1.txt","r")
content = f.read()
print(content)
"""

"""
tell() -> 
1. it returns cursor position in a file.
2. by default cursor always at the 0th position.

f = open("demo.txt","r")
print(f.tell())
t = f.read(6)
print(t)
print(f.tell())
t = f.read(9)
print(t)
print(f.tell())
f.close()

seek() ->
1. it will support to transfer a cursor to a required position in a file.
2. it also supports to move the cursor position in forward and backward direction.

syntax: file_variable.seek(offset, whence)

-> offset specifies a number of bytes to move.
-> whence specifies with 0, 1 and 2 i.e. position in a file
0 -> means beginning of a file.
1 -> means current position in a file.
2 -> means end of file.

# move the cursor position and then print content you can do that also.
f = open("demo.txt","r")
print(f.tell())
f.seek(6,0)
print(f.tell())
f.seek(15,0)
print(f.tell())
f.seek(17,0)
t = f.readline()
print(t)
f.close()


lst = ["python language\n","developed by\n","guido van rossum\n","In Netherlands\n"]
with open("demo.txt", "w") as f:
    f.writelines(lst)

with open("demo.txt", "r") as f:
    content = f.read()
    position = content.find("guido")
    print(position)


f = open("demo.txt", "r+")

print(f.tell())        # 0 (shuru mein cursor start pe hai)
f.seek(31, 0)           # "guido" ke exact start pe jao
print(f.tell())         # 29
f.write("?????")        # "guido" (5 chars) ko "?????" (5 chars) se replace
f.seek(0, 0)            # cursor ko wapas start pe le jao, taaki poori file padh sako
content = f.read()
print(content)
f.close()
"""

"""
# how to play with offset and whence
with open("demo.txt","r") as f:
          print(f.tell())
          f.seek(6,0) # moves cursor from beginning to 6th position in the file
          print(f.tell())
          t = f.readline()
          print(t)
          f.seek(0,0) # move cursor again from beginning of the file
          t = f.read()
          print(t)

# how to move forward
with open("demo.txt","rb") as f:
          print(f.tell())
          # move forward with positive offset
          f.seek(6,1) # move from current position by 6 characters
          t = f.read(9)
          print(t)

# how to move backward
with open("demo.txt","rb") as f:
          print(f.tell())
          f.seek(17,1) # move from current position by 17 characters
          print(f.tell())
          # move backward with negative offset
          f.seek(-11,1)
          t = f.read(9)
          print(t)

Important: whence=1 ke saath negative offset use karne ke liye file binary mode (rb, rb+) mein honi chahiye. Text mode (r, r+) mein Python sirf seek(0, 1) allow karta hai negative/relative seeking ke saath — error dega:

python
f = open("demo.txt", "r")
f.seek(-5, 1)
# Error: can't do nonzero cur-relative seeks

Isiliye jab bhi forward/backward relative movement chahiye, binary mode use karo.

# when we want to take out some position from the last
f = open("demo.txt", "rb")

f.seek(-10, 2)        # end se 10 bytes PEECHE jao
print(f.tell())       # kuch position, end se 10 pehle

data = f.read()       # yahan se end tak sab padho
print(data)    

# alternative for getsize() function of os module
f = open("demo.txt","rb")
f.seek(0, 2)          # bilkul end pe jao
print(f.tell())        # ye poori file ki size (bytes) bata dega!
t = f.read()
print(t)
f.close()


import os
size = os.path.getsize("demo.txt")
print(size)
"""

"""
# working with r+ w+ and a+

lst = ["this is python world\n","Here you will learn everything that you needed\n"]
with open("demo.txt", "w") as f:
        f.writelines(lst)

with open("demo.txt","r") as f:
        t = f.read()
        print(t,end='')

with open("demo.txt","r+") as f:
        print(f.tell())
        t = f.read()
        print(t,end='')
        print(f.tell())
        f.write("this is kartik khade from python software foundation\n")

w+ -> write and read and it is a vulnerable if file has some content already
f = open("demo.txt", "w+")
f.write("Hello World")
f.seek(0)
print(f.read())
f.close()


a+ -> append and read

f = open("demo.txt", "a+")
print(f.tell())        # ye kya print karega, 0 ya kuch aur?
f.write("New Line Added\n")
f.seek(0)
print(f.read())
f.close()
"""

"""
f = open("demo.txt", "w+")   # sirf open kiya, kuch likha/padha nahi
f.close()

f = open("demo.txt", "a+")
f.write("Appended Text\n")
data = f.read()
print(repr(data))
f.close()

f = open("test.txt", "w+")
f.write("AAA")
print(f.tell())
f.seek(0)
f.write("BB")
print(f.tell())
f.seek(0)
print(f.read())
print(f.tell())
f.close()
"""
