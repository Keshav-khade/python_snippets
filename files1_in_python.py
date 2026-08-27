# make a text file and write some text in it.
"""
# gives some useful information about the file

f = open("demo.txt","w")
print(f.name)
print(f.mode)
print(f.writable())
print(f.readable())
print(f.closed)
print(f.encoding)
f.close()
print(f.closed)
"""

"""
# how to write something in a file

f = open("demo.txt","w")
str = input("Enter you text: ")
f.write(str)
f.close()
"""

"""
# how to read data from a text file

f = open("demo.txt","r")
t = f.read()
print(t)
f.close()
"""

"""
# how to append data from a file

f = open("demo.txt","a")
f.write("this is second line of demo.txt file")
f.write("this is third line of demo.txt file")
f.close()
"""

"""
# how to write a content in new line every time

f = open("demo.txt","w")
f.write("this is second line of demo.txt file\n") # write only take string as an argument
f.write("this is third line of demo.txt file\n")
f.close()
"""

"""
# how to write multiple line of text in text file

f = open("demo.txt",'a')

lst = ["python language\n","developed by\n","guido van rossum\n","in Netherlands\n"]
f.writelines(lst) # writelines takes any iterable as an argument
f.close()
"""

"""
f = open("demo1.txt","w")
flag = True
while flag:
          str = input("Enter your text: ")
          f.write(str + "\n")
          res = input("do you want to write more (Y/N): ")
          if res.lower() in "no":
                    flag = False
f.close()
"""

"""
# preceding code with optimized approach

with open("demo.txt","w") as f:
          while True:
                    str = input("Enter your text: ")
                    f.write(str + "\n")
                    res = input("do you want to write more (y/n): ")
                    if res.lower() == "n":
                              break
"""

"""
# where to use file opening mode x
1. it only lets you create new file if you want to write in existing file it will throw you fileexistsError.

fn = input("Enter you file name with extension: ")
f = open("demo2.txt","x")

while True:
          ln = input("Enter text to store or Enter to end: ")
          if len(ln) == 0:
                    break
          f.write(ln + '\n')
f.close()
"""

"""
read() -> entire text from a specified file.
# reads entire content from the file as a string

with open("demo.txt", "r") as f:
    content = f.read()
    print(content)
    print(type(content))
"""

"""
read(n) -> reads n characters from a specified file as a bytes. in this method cursor positions remembered by the os from where it left, starts from there only not from beginning of the file.

with open("demo.txt", "r") as f:
    part1 = f.read(6)
    print(part1)
    print("---")
    part2 = f.read(9)
    print(part2)
"""

"""
readline() -> 
1. reads line of text from a specified file. on every call it reads new line from a specified file.
2. reads one line until it found \n newline character.
3. every call moves cursor on next new line.
4. when file gets empty it returns "" empty string which tell python about file ending.

with open("demo.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(repr(line1))   # repr() se \n dikhega clearly
    print(repr(line2))
print()

with open("demo.txt","r") as f:
    while True:
          ln = f.readline()
          if ln == "":
               break
          print(ln.strip()) #trimming up extra newlines 
"""

"""
4. readlines() -> 
1. read multiple lines of text from a text file.
2. returns list of strings with newline escape character
3. 

with open("demo.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    print(type(lines))

with open("demo.txt","r") as f:
    lines = f.readlines()
    for ln in lines:
        print(ln.strip())

with open("demo.txt","r") as file:
          for ln in file:
                  print(ln.strip())

this code is very memory efficient because it doesn't load all file content into the ram instead it load one line at a time so if it 1mb file or 100gb file doesn't matter.                  
with open("bigfile.log", "r") as f:
    for line in f:        # ek time pe sirf ek line RAM mein aati hai
        process(line)
"""

"""
repr -> 
1. returns a developer friendly string object representation.
2. it help developers to know that how strings are stored internally in their actual form.

with open("demo.txt","r") as f:
    lines = f.readlines()
    for ln in lines:
        print(repr(ln))

# Demonstrating repr() with strings

# Normal string
s1 = "Hello World"
print("Using str():", str(s1))
print("Using repr():", repr(s1))

# String with special characters
s2 = "Hello\nWorld\t!"
print("\nUsing str():", str(s2))
print("Using repr():", repr(s2))

# String with quotes
s3 = 'He said, "Python is fun!"'
print("\nUsing str():", str(s3))
print("Using repr():", repr(s3))

# Showing that eval(repr(obj)) recreates the object
original = "Line1\nLine2"
recreated = eval(repr(original))
print("\nOriginal equals recreated?", original == recreated)
"""


"""
# write a program to input source file. input target file. copy the text from source file to target file. Display the content from target file.

sf = input("Enter your source file")
tf = input("Enter your target file")

with open("demo.txt","r") as file:
        content = file.read()

with open("demo1.txt","w") as file:
        file.write(content)

with open("demo1.txt","r") as file:
        content = file.read()
        print(content)
"""

"""
# write a program to input 3 files. concatenate text from 2 files into a single file.
display the content from target file.

sf1 = input("Enter source file: ")
sf2 = input("Enter source file: ")
tf = input("Enter target file: ")

with open(sf1,"r") as f1:
        content1 = f1.read()

with open(sf2,"r") as f2:
        content2 = f2.read()

with open(tf, "w") as f3:
        f3.write(content1 + content2)
"""

"""
# file1 ko file2 mein directly append karo

with open("demo.txt", "r") as f1, open("demo1.txt", "r") as f2, open("file1.txt","a") as f3:
    for line in f1:
        f3.write(line)
    for line in f2:
        f3.write(line)
"""

"""
# how to merger more than one file using for loop

# create a list of files
str = input("Enter you file names along with extension and space: ")
lst = str.split()

with open("merged.txt","w") as outfile:
        for fname in lst:
            with open(fname,"r") as infile:
                outfile.write(infile.read())
                outfile.write("\n")

f = open("merged.txt","r")
t = f.read()
print(t)
f.close()
"""

"""
# this module helps us to copy large files into another file , memory efficient script.
# it helps to copy chunks of data from one file to another file instead of getting entire file into ram.
import shutil

with open("merged.txt", "wb") as outfile:
    for fname in ["file1.txt", "file2.txt"]:
        with open(fname, "rb") as infile:
            shutil.copyfileobj(infile, outfile)
"""