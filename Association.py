"""
"What is association?"

Say:
"Association is a relationship between two independent objects where one object uses or communicates with another object. Aggregation and composition are specialized forms of association with stronger ownership rules."

1.Every composition is an association, but every association is not composition.
2. association tells the relationship between objects, and they can use each other.
3. association is bigger picture of composition and aggregation.
3.1 One object interacts with another object to perform some action."

4.
OOP Relationship Hierarchy
                 Association
                      |
        +-------------+-------------+
        |                           |
   Aggregation                Composition

Meaning:

Association → General relationship
Aggregation → Stronger form of association
Composition → Strongest form of association
So:
Composition ⊂ Aggregation ⊂ Association

5. example of association can be, Teacher -> student they can exist without each other but teacher can use student class.


"""

"""
class Customer:
    def __init__(self,pro_ref):
        self.customer_id = ""
        self.customer_name = ""
        self.pro_ref = pro_ref
        self.ord_ref = Orders()
 
    def login(self, cus_id, cus_name):
        self.customer_id = cus_id
        self.customer_name = cus_name

    def get_ref(self, pro_ref, ord_ref=None):
        self.ord_ref = ord_ref
        self.pro_ref = pro_ref

    def place_order(self,ord_date):
        status = self.ord_ref.make_order(self,self.customer_id,ord_date)
        print(status)

    def is_order(self, ord_ref):
        flag = False
        if self.ord_ref is ord_ref:
            flag = True
        return flag


class Product:
    def __init__(self):
        self.pro_id = 0
        self.pro_name = ""

    def set_product(self, pro_id, pro_name):
        self.pro_id = pro_id
        self.pro_name = pro_name

    def display(self):
        return f"pro_id: {self.pro_id}\tpro_name: {self.pro_name}"


class Orders:
    def __init__(self):
        self.order_id = ""
        self.order_date = ""
        self.order_list = []
        self.order_status = []

    def make_order(self, cus_ref, ord_id, ord_date):
        self.order_id = ord_id
        self.order_date = ord_date
        self.order_list.append({"cus_ref":cus_ref, "ord_id":ord_id,"ord_date":ord_date})
        self.order_status.append({"ord_id":ord_id,"ord_status":cus_ref.is_order(self)})
        pay = Payment()
        pay_m = input("Enter payment method(UPI/CASH/DEBIT/CREDI): ")
        pay.payment(cus_ref,self,pay_m,ord_date)
        return pay.get_payment_status()

class Payment:
    def __init__(self):
        self.pay_id = 0
        self.ord_id = ''
        self.pay_method = ''
        self.pay_date = ''
        self.pay_status = []

    def payment(self, cus_ref, ord_ref, pay_method, pay_date):
        self.pay_id = cus_ref.customer_id
        self.ord_id = ord_ref.order_id + f"/{cus_ref.customer_name}"
        self.pay_method = pay_method
        self.pay_date  = pay_date
        self.pay_status.append({self.pay_id,self.ord_id,self.pay_method,self.pay_date})

    def get_payment_status(self):
        return self.pay_status

# product purchase
p1 = Product()

cus_id = input("Enter your id: ")
cus_name = input("Enter your name: ")
# creating customer
c1 = Customer(p1)
# logging in
c1.login(cus_id, cus_name)

# set product
pro_id = input("Enter product id: ")
pro_name= input("Enter product id: ")

p1.set_product(pro_id,pro_name)

# order something
c1.place_order("05/08/2026")
"""