# LRU Cache
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, u_id):
        if u_id not in self.cache:
            return None
        self.order.remove(u_id)
        self.order.append(u_id)
        return self.cache.get(u_id,"not found")

    def put(self,user_d, value):
        if user_d in self.cache:
            self.order.remove(user_id)
            self.order.append(user_id)
            self.cache[user_id] = value
            return
        if len(self.cache) >= self.capacity:
            val = self.order.pop(0)
            del self.cache[val]

        self.cache[user_id] = {"name":value}
        self.order.append(user_id)

class Database:
    def __init__(self):
        self.user_db = {}

    def add_user(self, u_details):
        """feeding database with users"""
        key = u_details.pop("user_id", None)
        self.user_db[key] = u_details

    def get_user_detail(self,lru_ref,u_id):
        cached_value = lru_ref.get(u_id)

        if cached_value is not None:
            print(f"[cache HII]: for user id: {u_id} --> {cached_value}")
            return cached_value

        print(f"[Db HIT]: for user id: {u_id} ---> {self.user_db[u_id]["name"]}")
        value = self.user_db[u_id]["name"]
        lru_ref.put(u_id,value)
        return value

class User:
    def __init__(self):
        self.user_id = 0
        self.user_name = ""

    # login logic
    def login(self, db_ref):
        self.user_id = int(input("Enter your user id: "))
        self.user_name = input("Enter your user name: ")
        # add users into the database
        temp_dict = dict()
        temp_dict.update({"user_id":self.user_id, "name":self.user_name})
        db_ref.add_user(temp_dict)

    def get_user(self, lru_ref, db_ref):
        res = db_ref.get_user_detail(lru_ref,self.user_id)
        return res

# creating database object
database = Database()

# creating LRU object
lru = LRUCache(capacity=39)

# remembering all the users
user_lst = {}
# Database feeding by users and their id's
while True:
    choice = input("do you want to add more users (Y/N): ")
    if choice in "Yy":
        # everytime creates a new user
        user = User()
        # adding users to database
        user.login(database)
        user_lst[user.user_id] = user
    else:
        break

user_id = int(input("Enter your user id: "))
ref = user_lst[user_id]
name = ref.get_user(lru,database)
print(name)
name1 = ref.get_user(lru,database)
print(name)