fake_database = {
    100: "kartik",
    101: "ravi",
    102: "Keshav",
    103: "ram"
}

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self,user_id):
        if user_id in self.cache:
            self.order.remove(user_id)
            # most recently used
            self.order.append(user_id)
            # if present then give away
            return self.cache[user_id]
        # if not present tell None
        return None

    def put(self,user_id, value):
        if user_id in self.cache:
            """this ensures that this value is most recently called so modify it in order"""
            self.cache[user_id] = value
            self.order.remove(value)
            self.order.append(value)
            return
        if len(self.cache)  >= self.capacity:
            # pop out the least recently used key from order which remember behaviors
            index = self.order.pop(0)
            # cache is about to full evict that oldest key from both order and cache
            del self.cache[index]

        self.cache[user_id] = {"name":value}
        self.order.append(user_id)

# create cache instance
lru = LRUCache(capacity=39)
def get_user(user_id):
    result = lru.get(user_id)
    # if user in cache least recently used
    if result is not None:
        return result

    # ask database to give user
    val = fake_database.get(user_id, "user not in db")
    lru.put(user_id, val)
    return val

user_id = int(input("Enter user id: "))
res = get_user(user_id)
print(res)
res1 = get_user(user_id)
print(res1)