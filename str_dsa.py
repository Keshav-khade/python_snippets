# import re

"""
# check if a string is palindrome or not
s = '121'
copy = [str(i) for i in s]
start = 0
end = len(s)-1
while start <= end:
          temp = copy[start]
          copy[start] = copy[end]
          copy[end] = temp
          start += 1
          end -= 1
copy = "".join(copy)
print("palindrome" if copy == s else "not palindrome")


# same question with two pointer just compare and check
s = 'madam'
start = 0
end = len(s) - 1
is_palindrome = True
while start <= end:
    if s[start] != s[end]:
        is_palindrome = False
        break
    start += 1
    end -= 1
print("palindrome" if is_palindrome else "not palindrome")



# recursive approach
def is_palindrome(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return is_palindrome(s, start + 1, end - 1)
s = 'madam'
print("palindrome" if is_palindrome(s, 0, len(s)-1) else "not palindrome")


# using stack base approach
s = 'madam'
stack = []
for ch in s:
    stack.append(ch)
reconstructed = ""
while stack:
    reconstructed += stack.pop()
print("palindrome" if reconstructed == s else "not palindrome")
"""


"""
count the vowels and consonants in a string

s = "KARTIK KHADE"
vowel_cnt = 0
consonant_cnt = 0
s = s.lower()
vowels = "aeiou"
for ind in range(len(s)):
          if s[ind] in vowels:
                  vowel_cnt += 1
          if 97 <= ord(s[ind]) <= 122 and s[ind] not in vowels:
                  consonant_cnt += 1
print(f"vowels is: {vowel_cnt}\tconsonants is:{consonant_cnt}")

# second approach
s = "Hello World"
s = s.lower()
vowels = "aeiou"
vowel_cnt = 0
consonant_cnt = 0
for ch in s:
    if ch in vowels:
        vowel_cnt += 1
    elif ch.isalpha():
        consonant_cnt += 1
print(f"vowels is: {vowel_cnt}\tconsonants is:{consonant_cnt}")


# using built-ins count() which counts the occurrence of a given element in a iterator
s = "Hello World"
s = s.lower()
vowels = "aeiou"
vowel_cnt = sum(s.count(v) for v in vowels)
consonant_cnt = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
print(f"vowels is: {vowel_cnt}\tconsonants is:{consonant_cnt}")
"""

"""
q3. reverse each word in a string

s1 = input("Enter a string: ")
lst = s1.split()
final_list = []
for s in lst:
    temp_list = list(s)
    start = 0
    end = len(temp_list) - 1
    while start <= end:
        temp = temp_list[start]
        temp_list[start] = temp_list[end]
        temp_list[end] = temp
        start += 1
        end -= 1
    temp_s = "".join(temp_list)
    final_list.append(temp_s)
s1 = " ".join(final_list)
print(s1)


# second approach to do same work
new = input("Enter a string: ")
words = new.split()
reversed_str = [word[::-1] for word in words]
res = " ".join(reversed_str)
print(res)
"""

""" 

# first method using character
s = input("Enter a string: ")
char = input("Enter a character: ")
count = 0
for ch in s:
    if ch == char:
        count += 1

print(f"character {char} appears {count} times")

# second method 
count1 = s.count(char)
print(f"character {char} appears {count1} times")

# using generator expression
s = "banana"
char = "a"
count = sum(1 for ch in s if ch == char)
print(f"character {char} appears {count} times")

# using filter method
s = "banana"
char = "a"
count = len(list(filter(lambda ch: ch == char, s)))
print(f"character {char} appears {count} times")

# using regex
s = "banana"
char = "a"
count = len(re.findall(char, s))
print(f"character {char} appears {count} times")

# using dictionary 
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
# {'b': 1, 'a': 3, 'n': 2}
print(f"character a appears {freq.get('a', 0)} times")
"""

"""
# here is your q5 answer but it's quite space occupier

s1 = 'listen'
s2 = 'silent'
freq_d1 = dict()
freq_d2 = dict()
for i in range(len(s1)):
    if s1[i] in freq_d1:
        freq_d1[s1[i]] += 1
    else:
        freq_d1[s1[i]] = 1
for i in range(len(s2)):
    if s2[i] in freq_d2:
        freq_d2[s2[i]] += 1
    else:
        freq_d2[s2[i]] = 1
if freq_d1 == freq_d2:
    print("Anagram")
else:
    print("not")


s1 = 'listen'
s2 = 'silent'
freq = {}
if len(s1) != len(s2):
    print("not anagram")
else:    
    for ch in s1:
        freq[ch] = freq.get(ch,0) + 1

    for ch in s2:
        freq[ch] = freq.get(ch,0) - 1

    is_anagram = all(count == 0 for count in freq.values())
    print("anagram" if is_anagram else "not anagram")


# using arrays list of fixed 26 characters of lower case

s1 = 'listen'
s2 = 'silent'
if len(s1) != len(s2):
    print("not")
else:
    count = [0] * 26   # one slot per letter a-z

    for ch in s1:
        count[ord(ch) - ord('a')] += 1
    for ch in s2:
        count[ord(ch) - ord('a')] -= 1

    is_anagram = all(c == 0 for c in count)
    print("Anagram" if is_anagram else "not")
"""

"""
Find the first non-repeating character in a string.

s = "aabb"
if len(s) == 0:
    print("None")
arr = [0]*26
for ch in s:
    arr[ord(ch)-ord('a')] += 1
flag = False
for ch in s:
    if arr[ord(ch) - ord('a')] == 1:
        print("first non-repeating character is: ",ch)
        flag = True
        break
if not flag:
    print("There is no such character is present")


s = "ssi"
if len(s) == 0:
    print("None")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0) + 1
result = None
for ch in s:
    if freq[ch] == 1:
        result = ch
        break
print(f"first non-repeating character is {result}" if result else "there is no such character present")
"""

"""
7. All Unique Characters (pure loops, no set/dict)

# fixed size array
s = "hello"
s = s.lower()
arr = [0]*26
for ch in s:
    arr[ord(ch)-ord('a')] += 1
flag = False
for val in arr:
    if val > 1:
        print("False")
        flag = True
        break
if not flag:
    print("True! all unique")

# nested loop based
s = "hello"
is_unique = True
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            is_unique = False
            break
    if not is_unique:
        break
print("True! all unique" if is_unique else "False")
"""

"""
8. Remove Duplicate Characters (preserve first-occurrence order)


# case in-sensitive approach
s = "Kartik"
final = ""
seen = ""
for ch in s:
    if ch in seen:
        continue
    seen += ch.lower()
    final += ch
print(final)

# you can also use sets here coz their lookup order is also same
s = "Kartik"
final = ""
seen = set() # seen = {} also represent set
for ch in s:
    if ch in seen:
        continue
    seen.add(ch.lower())
    final += ch
print(final)
"""

"""
run length encoding

# s = "aaaa"
# s = "aabbccaa"
# s = "aabba"
# s = ""

if not s:
        print("empty")
else:
        
          final = ""
          count = 1

          for i in range(1, len(s)):
                    if s[i] == s[i-1]:
                              count += 1
                    else:
                              final += s[i-1] + str(count)
                              count = 1
          final += s[-1] + str(count)
          print(final)
"""

"""
Check if a string is a rotation of another string ("abcd" and "cdab" → True)

original = 'abcd'
rotated = 'cdab'

if len(s1) != len(s2):
    print("False")
else:
    lst = list(original)
    rotation = len(lst)

    is_rotated = False
    while rotation > 0:
        i = len(lst) - 1
        temp = lst[i]
        while i > 0:
            lst[i] = lst[i-1]
            i -= 1
        lst[0] = temp
        rotation -= 1
        
        s = "".join(lst)
        if rotated == s:
            print(f"{rotation} rotations")
            is_rotated = True
            break
    print(True if is_rotated else False)

# second approach for the same logic
s1 = 'abcd'
s2 = 'cdab'

if len(s1) != len(s2):
    print("False")
else:
    combined = s1 + s1   # "abcdabcd"
    if s2 in combined:
        print("True")
    else:
        print("False")
"""

"""

"""
