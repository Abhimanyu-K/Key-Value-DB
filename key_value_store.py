class KeyValueStore:
    def __init__(self):
        self.store = {}
        self.ttl = {}

    def set(self, key, value):
        self.store[key] = value
        return self.store[key]

    def get(self, key):
        if self.store.get(key):
            return self.store[key]
        else:
            return "Error: Key Not Found!"

    def delete(self, key):
        if self.store.get(key):
            del self.store[key]
            return "OK"
        return "Error: key not found"

    def incr(self, key, num=1):
        self.store[key] = int(self.store[key]) + num
        return self.store[key]

    def decr(self, key, num=1):
        self.store[key] = int(self.store[key]) - num
        return self.store[key]
