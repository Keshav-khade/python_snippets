# JSON FILE HANDLING
"""
q1. what is the full form of JSON ?
-> JavaScript object notation.

q2. what is JSON ?
->  1. JSON is a text file for representing data.
    2. JSON is a lightweight data interchange format
    3. JSON is platform independent file
    4. JSON is mostly used to transfer the data across multiple languages.
    5. JSON always provides the data in the form of key, value pairs.
    6. in real world applications to transfer data across languages following types of files are used.
        1. XML -> (extensible markup language) -> data represented with tag, it is heavyweight.
        2. JSON -> (JavaScript object notation) -> data represented through key, value pairs and it is lightweight.

q3. is there any module for working with JSON FILES ?
-> python provides a module called json to work with this file.

q4. data types that we can use in JSON ?
-> [objects {}, arrays [], strings , booleans, numbers, Null]

data in XML
<Employee>
    <Empid>100</Empid>
    <Ename>Keshav</Ename>
    <Salary>100000</Salary>
    <Deptid>10</Deptid>
</Employee>

data in JSON
{
    "Employee":{
            "Empid":100,
            "Ename":"kartik"
            "salary":100000
            "Deptid":10
    }
}
Employee -> object here
[Ename, Empid, salary, deptid] -> keys
[100, kartik, 100000, 10] -> values
"""

"""
{
    "order_id": "ORD-20938",
    "customer": {
        "id": 4521,
        "name": "Kartik Sharma",
        "email": "kartik@example.com",
        "is_premium_member": true,
        "loyalty_points": 340
    },
    "items": [
        {
            "product_id": "P-101",
            "name": "Wireless Mouse",
            "price": 799.50,
            "quantity": 2,
            "tags": ["electronics", "accessories"]
        },
        {
            "product_id": "P-205",
            "name": "USB-C Cable",
            "price": 299.00,
            "quantity": 1,
            "tags": ["electronics", "cables"]
        }
    ],
    "shipping_address": {
        "street": "221B Baker Street",
        "city": "Indore",
        "state": "Madhya Pradesh",
        "pincode": "452001",
        "landmark": null
    },
    "payment": {
        "method": "UPI",
        "status": "completed",
        "transaction_id": "TXN998877",
        "amount_paid": 1898.00
    },
    "is_gift": false,
    "discount_code": null,
    "order_date": "2026-08-15T10:30:00Z"
}

json object ->  it's a plain text file format
                representing triple double quotes
                1. keys must having strings with double quotes
                2. values are going to be {} object, array [], bool in small case true/ false
                3. numbers (int/float)
                4. supported nested object values also
                5. fields containing null value means field exists but having empty values

# ex.1 create a json structure, json is just a plain text with data type string
json = ''' {
    "Employee":{
        [
            {"empid":100, "ename":"kartik","salary":20000},
            {"empid":101, "ename":"keshav","salary":10000}
        ]
    }
}'''
print(type(json))
"""

"""
how json data formatting works
import json

order = {
    "order_id": "ORD-20938",
    "customer": {
        "id": 4521,
        "name": "Kartik Sharma",
        "is_premium_member": True,
        "loyalty_points": 340
    },
    "shipping_address": {
        "city": "Indore",
        "landmark": None
    },
    "is_gift": False,
    "discount_code": None
}

print(json.dumps(order, indent=4))

here,-> we have None in python -> in json it's null after converting it to json file
-> upper case False and True -> convert it to false/true
-> no trailing commas and no leading zeros should be there in json file while working with numbers and objects
"""

"""
json file handling: how to dump data into json file

import json
# q. creating a dictionary object in python and dump it into json format
d = {"name":"Keshav", "empid":1001, "location":"Bangalore", "salary": 100000}

json_str = json.dumps(d, indent=4)
print(json_str)
print(type(json_str))

# create a json file and store above data into it
with open("json_file.json","w") as f:
    json.dump(d, f, indent=4)
"""

"""
if you want to modify json structure first load it into memory than change it then dump back to it's original position.

ex.
import json
d = {"name":"Keshav", "empid":1001, "location":"Bangalore", "salary": 100000}

with open("employ.json","w") as f:
    json.dump(d, f, indent=4)

# this operation might breaks the json structure
with open("employ.json","a") as f:
    f.write('{"address":"Indore"}')

# how can we do that modification
# load the file into python object
with open("employ.json","r") as f:
        data = json.load(f)

data["address"] = "Indore"

# dump it back to the file
with open("employ.json", "w") as f:
    json.dump(data, f, indent=4)
"""

"""
Q. write a program to create a list of dictionaries with key value pairs and convert it into json

import json
lst = [{"name":"Keshav", "marks":{"english":85,"math":90}},{"name":"eva", "marks":{"english":85,"math":90}}]

f = open("file1.json","w")
json.dump(lst,f,indent=4)
f.close()

f = open("file1.json","r")
data = json.load(f)
f.close()

json_temp = json.dumps(lst,indent=4)
print(json_temp)
"""

"""
csv to json

# csv to JSON
import csv
import json
lst = [("Empid","Ename","salary","deptid"),(100,"kartik",10000,10),(200,"Keshav",20000,20),(300,"Keshav",20000,20),(400,"Keshav",20000,20)]

with open("temp1.csv","w", newline="") as f:
    w = csv.writer(f)
    w.writerows(lst)

with open("temp1.csv","r", newline="") as f1, open("temp2.json", "w") as f2:
    r = csv.DictReader(f1)
    data = list(r)
    json.dump(data,f2,indent=4)

with open("temp2.json", "r") as f:
    data = json.load(f)

data = json.dumps(data,indent=4)
print(data)
"""