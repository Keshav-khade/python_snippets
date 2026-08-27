"""
q1. list comprehension

x = int(input())
y = int(input())
z = int(input())
n = int(input())

# complexity o(n^3)
# for i in range(0, x+1):
#     for j in range(0, y+1):
#         for k in range(0, z+1):
#             if i+j+k != n:
#                 lst.append([i,j,k])

# using list comprehension
resultant = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(resultant)
"""

"""
q2. 
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

value = student_marks.get(query_name,None)
if value is not None:
    n = len(value)
    sum = 0
    for i in value:
        sum += i
    avg = sum/n
print(f"{avg:.2f}")
"""

"""
q3.
def wrapper(f):
    def fun(l):
        formatted = []
        for num in l:
            valid_n = num[-10:]
            modified_num = "+91" + " " + valid_n[:5] + " " + valid_n[5:]
            formatted.append(modified_num)
        f(formatted)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
"""


