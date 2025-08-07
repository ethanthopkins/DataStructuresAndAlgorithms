class MyHashTable:
    def __init__(self, initialCapacity = 10):
        self.table = []
        for i in range(initialCapacity):
            self.table.append([])
    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for i, (k, v) in enumerate(bucket_list):
            if k == key:
                bucket_list[i] = (key, value)
                return
        bucket_list.append((key, value))
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for k, v in bucket_list:
            if k == key:
                return v
        return None
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for i, (k, v) in enumerate(bucket_list):
            if k == key:
                del bucket_list[i]
                return
        return