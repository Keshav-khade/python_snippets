# """Develop single responsibility principal"""
import json
class Customer:
    def __init__(self):
        self.customer_id = ""
        self.customer_name = ""

    def login(self, cus_id, name):
        self.customer_id = cus_id
        self.customer_name = name

    def view_product(self, product):
        products = product.products()
        print(products)

    def select_product(self, product):
        pass

class Product:
    def __init__(self):
        self.pro_list = []
        self.set_of_dicts = set()

    def set_product(self, **kwargs):
        for key, val in kwargs.items():
            self.pro_list.append({key:val})

    def get_product(self):
        """efficient lookup on sets"""
        self.set_of_dicts = {json.dumps(d, sort_keys=True) for d in self.pro_list}
        pro_token = None
        for d in self.set_of_dicts:
            for key in d.keys():
                pro_token = key




    def check_stock(self, pro_name):
        for d in self.set_of_dicts:
            if pro_name in d:
                print(f"item in stock: {pro_name}")

class Orders:
    def __init__(self):
        self.order_id = ""
        self.order_date = ""
        self.order_list = []

    def create_ord(self, customer, product):
        temp_dict = dict()
        cus_id = customer.customer_id
        cus_name = customer.customer_name

        ord_id = product.get_product()

class Payment:
    pass




