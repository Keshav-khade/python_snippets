"""
# Exercise.1 before moving forward

inventory = {"pen": 50, "pencil": 30, "eraser": 20}

val = inventory.get("pencil",0)
# addition
inventory["marker"] = 15
# another way of addition
inventory.update({"marker":15})
# update or mutation
inventory["pen"] = 45
# deletion
value = inventory.pop("eraser")
print(value)
# searching
key = "sharpener"
if key in inventory:
    print("yes in")
else:
    print("not in")
"""

"""
# Exercise.2
students = {
    "s1": {"name": "Aman", "age": 20, "marks": 85},
    "s2": {"name": "Riya", "age": 21, "marks": 90}
}

# direct chaining
val = students["s1"]["name"]
print(val)

# safer check on nested dictionary chaining values
val1 = students.get("s3",{}).get("name")
print(val1)

students = {
    "s1": {"name": "Aman", "age": 20, "marks": 85},
    "s2": {"name": "Riya", "age": 21, "marks": 90}
}

students["s1"]["city"] = "Indore"
students["s2"]["city"] = "Hyderabad"

# adding a new student
students["s3"] = {"name":"kartik","age":"21","marks":86,"city":"Pune"}

# update s1
students["s1"]["marks"] = 95

# deletion
del students["s1"]["marks"]
# particular key deletion
city = students["s3"].pop("city")

# deleting entire student listings
des = students.pop("s1")

print(des)
print(city)
print(students)
"""

"""
students = {
    "s1": {"name": "Aman", "age": 20, "is_active":True, "marks": 85},
    "s2": {"name": "Riya", "age": 21, "is_active":False, "marks": 90}
}

# iteration using nested structure
for student_id, details in students.items():
    print(f"{student_id}:")
    for field, value in details.items():
        print(f"   {field}: {value}")
    print()   # blank line between students

# avoiding (n*m) complexity
for student_id, details in students.items():
    print(f"{student_id}: Name={details['name']}, Age={details['age']}, Marks={details['marks']}")

# useful in logging and writing to a file
for student_id, details in students.items():
    description = ", ".join(f"{k}={v}" for k, v in details.items())
    print(f"{student_id}: {description}")


with full description
for stud,details in students.items():
    print(f"{stud}: ")
    for field,value in details.items():
        print(f"\t{field}={value}")

# use isinstance(value,type) | instead type(value) == int : 
for stud,details in students.items():
    print(f"{stud}: ")
    for field,value in details.items():
    ""isinstance(value,bool) because True and False are the sub class of integer so it's gets True""
        if isinstance(value,int) and not isinstance(value,bool):
            print(f"\t{field}={value}")
"""

"""
company = {
    "engineering": {
        "backend": {
            "lead": "Keshav",
            "members": ["Riya", "Karan","eva"],
            "budget": 50000
        },
        "frontend": {
            "lead": "Neha",
            "members": ["Sara","pooja","madly"],
            "budget": 30000
        }
    },
    "sales": {
        "domestic": {
            "lead": "Vikram",
            "members": ["Pooja","sakshi"],
            "budget": 20000
        }
    }
}

# function for fetching safely at any nested level without bothering time and space complexity
def safe_get(d,keys,default="N/A"):
    current = d
    for key in keys:
        if isinstance(current,dict) and key in current:
            current  = current[key]
        else:
            return default
    return current

key = ["engineering","backend","budget"]
print(safe_get(company,key))
"""

"""
company = {
    "engineering": {
        "backend": {
            "lead": "Keshav",
            "members": ["Riya", "Karan","eva"],
            "budget": 50000
        },
        "frontend": {
            "lead": "Neha",
            "members": ["Sara","pooja","madly"],
            "budget": 30000
        }
    },
    "sales": {
        "domestic": {
            "lead": "Vikram",
            "members": ["Pooja","sakshi"],
            "budget": 20000
        }
    }
}

# direct chaining
emp_name = company["engineering"]["backend"]["lead"]
print(type(emp_name))

# extracting all the members of a team
emp_lst = company["engineering"]["backend"]["members"]
emp_lst.append(emp_name)
print(emp_lst)

# direct chaining but any level missing will raise KeyError
budget = company["engineering"]["frontend"]["budget"]
print(type(budget))
print(budget)

# without disturbing any level safely fetching
budget = company.get("engineering",{}).get("backend",{}).get("budget",0)
print(type(budget))
print(budget)

# adding new field into backend, tech stack
company["engineering"]["backend"]["tech_stack"] = ["Python","Django"]
print(company)

# adding new role in engineering
company["engineering"]["mobile_dev"] = {"lead":"Mohini","members":["rahul","sumit","priya"],"budget":70000}

# traversing on a company dictionary  time complexity o(n^3)
for department,details in company.items():
    print(f"{department}:")
    for branch,description in details.items():
        print(f"\t{branch}: ")
        for field,value in description.items():
            print(f"\t\t{field}={value}")

# traversing on a dict in o(n^2)
for department,details in company.items():
    print(f"{department}:")
    for branch,description in details.items():
        print(f"\t{branch}: ")
        print(f"\t\tLead: {description["lead"]}\n\t\tMembers: {description['members']}\n\t\tBudget: {description['budget']}")

print(company)

# increase frontend development budget
company["engineering"]["frontend"]["budget"] = 60000

print(company)

# if company drops android development then
del company["engineering"]["mobile_dev"]
print(company)
"""

"""
# merging two nested structures
ex.1
existing_config = {
    "database": {"host": "localhost", "port": 5432},
    "cache": {"ttl": 60}
}

new_config = {
    "database": {"timeout": 30}
}
# data before merging 
print(existing_config)

# merging two nested structures
existing_config.update(new_config)

# data lose after merging
print(existing_config)

ex.2
# different way of same problem
merged = {**existing_config, **new_config}
print(merged)

# another way of doing same problem works like set union
merged = existing_config | new_config
print(merged)

"""

"""
ex.1
# problem with merge and update the content from one dictionary to another
dct1 = {"name":"kartik"}
dct2 = {"name":"Keshav"}
print(dct1)
print(dct2)
merge = dct1.update(dct2)
print(merge) # prints None becaue .update() update the dictionary object in-place

ex.2
# solution to this problem unpack the dictionaries and then perform merge and update operations. 
existing_config = {
    "database": {"host": "localhost", "port": 5432},
    "cache": {"ttl": 60}
}
new_config = {
    "database": {"timeout": 30}
}
# I want this same effect without overriding so i don't lose my data anymore
existing_config["database"].update(new_config["database"])
print(existing_config)

ex.3 How to develop a function which means reusable logic for nested insertion and updation
existing_config = {
    "d1":{
        "database": {"host": "localhost", "port": 5432},
    }
}
new_config = {
    "d1":{
        "database": {"timeout": 30}
    }
}

# more generalize approach with function reusable and faster deep merge
def deep_merge(d1,d2):
    ""build a temporary dictionary""
    result = dict(d1)
    # traverse on second dict and find the values that has to be merge
    for key,val in d2.items():
        ""check if d1 and d2 has same keys and their values would be dictionary objects""
        if key in result and isinstance(result[key], dict) and isinstance(val, dict):
            result[key] = deep_merge(result[key],val)
        else:
            result[key] = val
    return result

existing_config= deep_merge(existing_config,new_config)

print(existing_config)


ex.4 how to make more recursive call and modify the data at each level safely

a3 = {
    "company": {
        "engineering": {"budget": 50000, "lead": "Priya"}
    }
}
b3 = {
    "company": {
        "engineering": {"budget": 60000},
        "sales": {"budget": 20000}
    }
}

def deep_merge(d1,d2):
    ""build a temporary dictionary""
    result = dict(d1)
    # traverse on second dict and find the values that has to be merge
    for key,val in d2.items():
        ""check if d1 and d2 has same keys and their values would be dictionary objects""
        if key in result and isinstance(result[key], dict) and isinstance(val, dict):
            result[key] = deep_merge(result[key],val)
        else:
            result[key] = val
    return result

a3 = deep_merge(a3, b3)
print(a3)

ex.5
a4 = {
    "app": {
        "database": {
            "primary": {"host": "localhost", "port": 5432}
        }
    }
}
b4 = {
    "app": {
        "database": {
            "primary": {"port": 5433, "replicas": ["r1", "r2"]}
        },
        "cache": {"ttl": 60}
    }
}
def deep_merge(d1,d2):
    ""build a temporary dictionary""
    result = dict(d1)
    # traverse on second dict and find the values that has to be merge
    for key,val in d2.items():
        ""check if d1 and d2 has same keys and their values would be dictionary objects""
        if key in result and isinstance(result[key], dict) and isinstance(val, dict):
            result[key] = deep_merge(result[key],val)
        else:
            result[key] = val
    return result

a4 = deep_merge(a4, b4)

for key,val in a4.items():
    print(f"{key}: ")
    for key1,val1 in val.items():
        print(f'\t{key1}: ')
        for key2,val2 in val1.items():
            if isinstance(val2, int):
                print(f"{'\t'*3}{key2}: {val2}")
                break
            print(f"{'\t'*2}{key2}: ")
            print(f"{'\t'*3}port: {val2["port"]}\n{'\t'*3}replicas: {val2['replicas']}\n{'\t'*3}host: {val2['host']}")

"""

"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

"""
1.Given:
student = {
    "name": "Keshav",
    "marks": {"maths": 90, "science": 85},
    "address": {"city": "Indore", "pincode": "452009"}
}
Print the science mark and the city, using both direct access and .get() chains.

2. Add a new subject "english": 88 inside the nested "marks" dict.

3. Given a dictionary of dictionaries representing multiple students (like {"s1": {...}, "s2": {...}}), write a loop to print each student's name and total marks (sum of subject scores).

4. Given a 3-level nested dictionary:

data = {
    "company": {
        "dept": {
            "team": {
                "lead": "Priya"
            }
        }
    }
}

Write a generic function safe_get(d, *keys, default=None) that can fetch data["company"]["dept"]["team"]["lead"] safely without crashing if any intermediate key is missing.

5. Given a list of nested dicts (like the company["employees"] example from earlier), extract all unique skills across all employees into a single set.

6. Flatten a nested dictionary into a single-level dictionary with dotted keys. Example: {"a": {"b": 1, "c": 2}} → {"a.b": 1, "a.c": 2}. (Classic interview question — needs recursion.)

7. Given a nested dict representing a JSON-like API response, write code to update a deeply nested value without knowing the exact depth in advance (use recursion or a path list like ["a","b","c"]).

8. Merge two nested dictionaries deeply (not just top-level update, which overwrites nested dicts entirely) — e.g., {"a": {"x":1}} merged with {"a": {"y":2}} should give {"a": {"x":1, "y":2}}.
"""

"""
q1.
student = {
    "name": "Keshav",
    "marks": {"maths": 90, "science": 85},
    "address": {"city": "Indore", "pincode": "452009"}
}
# Print the science mark and the city, using both direct access and .get() chains.
# using direct access
science_marks = student["marks"]["science"]
city = student["address"]["city"]

print(science_marks)
print(city)

#using .get() safer method
science_marks = student.get("marks",{}).get("science","not found")
print(science_marks)

city = student.get("address",{}).get("city","not found")
print(city)
"""

"""
q2.
student = {
    "name": "Keshav",
    "marks": {"maths": 90, "science": 85},
    "address": {"city": "Indore", "pincode": "452009"}
}
def deep_merge(d1,d2):
    result = dict(d1)
    for key,val in d2.items():
        if key in result and isinstance(result[key], dict) and isinstance(val, dict):
            result[key] = deep_merge(result[key],val)
        else:
            result[key] = val
    return result

given_dict = {
    "marks":{
        "english":88
    }
}
student = deep_merge(given_dict, student)

print(student)
"""

"""
q3.
cls = {
    "s1":{"name":"sumit","marks":{"maths":90,"science":85,"english":82}},
    "s2":{"name":"kartik","marks":{"maths":94,"science":83,"english":85}},
    "s3":{"name":"ravi","marks":{"maths":95,"science":78,"english":79}},
}

for stud,details in cls.items():
    print(f"Name: {details["name"]}")
    print(f"Total_Marks: {sum(val for key,val in details["marks"].items())}")
"""

"""
q4.
data = {
    "company": {
        "dept": {
            "team1": {
                "lead": "Priya",
                "backend":["kartik","Keshav","ram","eva","captain"]
            },
            "team2":{
                "lead": "Ram",
                "frontend":{"Shubha","madhur","rani"}
            }
        }
    }
}
# data["company"]["dept"]["team"]["lead"]
def safe_get(d, keys, default=None):
    current = dict(d)
    for k in keys:
        if k in current and isinstance(current, dict):
            current = current[k]
        else:
            return default
    return current

key = ["company","dept","team2","frontend"]
res = safe_get(data, key)
print(res)
"""

"""
q5.
company = {
    "employees": [
        {"name": "Amit", "role": "Backend Dev", "skills": ["Python", "Django"]},
        {"name": "Sara", "role": "Frontend Dev", "skills": ["React", "JS"]},
        {"name": "Karan", "role": "Backend Dev", "skills": ["Python", "SQL"]}
    ]
}
unique_skills = set()
for details in company["employees"]:
    unique_skills.update(details["skills"])

print(unique_skills)
"""

"""
q6. logic for flatten the nested dictionaries into chaining 
d2 = {
    "user": {
        "address": {
            "city": "Indore",
            "pincode": "452001"
        },
        "name": "Keshav"
    }
}

def flatten(d,parent_key=""):
    result = {}
    for key, value in d.items():
        # build the key now
        new_key = parent_key + "." + key if parent_key else key
        if isinstance(value, dict):
            result.update(flatten(value, new_key))
        else:
            result[new_key] = value
    return result

result = flatten(d2)
print(result)
"""

"""
q8.
d1 = {"a": {"x":1}}
d2 = {"a": {"y":2}}

def merge(d1,d2):
    result = dict(d1) # "a": {"x":1,"y":2}
    for key,val in d2.items():
        if key in result and isinstance(result[key], dict) and isinstance(val, dict):
            result[key] = merge(result[key], val) #  {"x":1,"y":2}
        else:
            result[key] = val
    return result # {"x":1,"y":2}

# final result "a": {"x":1,"y":2}
res = merge(d1,d2)
print(res)
"""

"""I can do anything and everything if only when i believe in myself and be with myself"""

