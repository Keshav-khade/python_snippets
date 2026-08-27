# csv -> comma separated values
# 1. this is a pain text file format which stores data into tabular form

"""
we can also work without module but it quit inconvenience

with open("sample.csv","w+") as f:
          f.write("Empid,Ename,Salary,Deptid\n")
          f.write("1001,kartik,20000.32,10\n")
          f.write("1002,keshav,12000,12\n")
          f.write("1003,ram,18000,10\n")
          print(f.tell())

with open("sample.csv","r") as f:
        for row in f:
          for col in row:
           print(col,end="")  
"""

"""
# writerow handles one line at a time
with open("employees.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["empid", "ename", "salary", "deptid"])   # header
    writer.writerow([101, "Rahul", 45000, 10])
    writer.writerow([102, "Priya", 60000, 20])
    writer.writerow([103, "Aman", 38000, 10])
    writer.writerow([104, "Sneha", 72000, 30])
    writer.writerow([105, "Vikas", 55000, 20])
"""

"""
# writing multiple rows and column in one go
data = [
    ["empid", "ename", "salary", "deptid"],
    [101, "Rahul", 45000, 10],
    [102, "Priya", 60000, 20],
    [103, "Aman", 38000, 10],
]

with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)   # poori list of lists ek saath likh di
"""

"""
# every row is a list in reader object you can treat it like a nested list object
with open("employees.csv","r") as f:
          t = csv.reader(f)
          for ln in t:
             print(ln)

# using nested for loop you can traverse on every single column
with open("employees.csv","r") as f:
          t = csv.reader(f)
          for row in t:
             for col in row:
                    print(col,end='\t')
             print()
"""

"""
# how to read data into dictionary format where every row becomes dictionary
# DictReader consider first row as header and make them keys for your dictionaries.
with open("employees.csv","r") as f:
          dict_row = csv.DictReader(f)
          for row in dict_row:
                  print(row)
"""
import csv

# lst = [ 
# ['empid','ename','salary','deptid'],
# [101,'Rahul',45000,10],
# [102,'Priya',60000,20],
# [103,'Aman',38000,10],
# [104,'Sneha',72000,30],
# [105,'Vikas',55000,20]
# ]
# with open("employees.csv","w",newline='') as f:
#           writer = csv.writer(f)
#           writer.writerows(lst)

"""
# fetching only employee name from the list.
with open("employees.csv","r",newline='') as f:
          reader = csv.reader(f)
          next(reader)
          lst = []
          for row in reader:
              lst.append(row[1])
print(lst)

# find the maximum salary of an employee
with open("employees.csv","r",newline='') as f:
          reader = csv.reader(f)
          next(reader)
          max_salary = 0
          for row in reader:
              val = int(row[2])
              if val > max_salary:
                    max_salary = val
print(max_salary)

# find lowest paid employee among all
with open("employees.csv","r",newline='') as f:
          reader = csv.reader(f)
          next(reader)
          lst = list(reader)
          min_salary = int(lst[0][2])
          ename = ""
          for row in lst:
              val = int(row[2])
              if val < min_salary:
                    min_salary = val
                    ename = row[1]
print(f"Lowest paid Employee is: {ename}\nwith salary: {min_salary}")


# find employee who belongs to an specific department
dept_10_employees = []
with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["deptid"] == "10":
            dept_10_employees.append(row["ename"])
print("Dept 10 employees:", dept_10_employees)

# total salary of all employee and their average salary in rupees
with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    sum = 0
    count = 0
    for row in reader:
        count += 1
        sum = sum + int(row["salary"])
    avg = sum / count
print(f"Total salary of emplyees is: {sum}\nAverage income of a company is: {avg}")

# sort the employees based on their salary highest to lowest.
with open("employees.csv","r",newline='') as f:
        reader = csv.DictReader(f)
        emp_list = list(reader)
        final_list = sorted(emp_list, key=lambda row: row["salary"], reverse=True)
        for emps in final_list:
            print(emps["ename"],"\t",emps["salary"])

# employees who's salaries are greater than 50k
with open("employees.csv","r",newline='') as f:
        reader = csv.DictReader(f)
        emp_list = [row['ename'] for row in reader if int(row["salary"]) > 40000]
        print(emp_list)

# salary department wise (group by department)
with open("employees.csv","r",newline='') as f:
        reader = csv.DictReader(f)
        final_dict = {}
        for row in reader:
          dept = row["deptid"]
          salary = int(row["salary"])
          final_dict[dept] = final_dict.get(dept,0) + salary
print(final_dict)


# find the employee information using his name.
with open("employees.csv","r",newline='') as f:
        reader = csv.reader(f)
        ename = input("Enter employee name: ")
        flag = False
        for row in reader:
            str = ",".join(row).lower()
            if ename in str:
                flag = True
                print(row)
                break
        if not flag:
            print("Employee not found !")    
"""
# import os
# fn = input("Enter file name: ")
# if os.path.exists(fn):
#         print("yes this is a file")
# else:
#         print("this is not")
import os,sys
lst = ["this is python\n","I am the greatest\n"]
f = open("new.txt","w")
f.writelines(lst)
f.close()
cl = cw = cc = 0
with open("new.txt","r",newline='') as f:
        data = f.read()
        for ch in data:
            print(ch,end='')
        # words = data.split()

