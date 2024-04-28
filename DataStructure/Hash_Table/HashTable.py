class HashTable:
    def __init__(self):
        self.capacity = 10
        self.arr = [None for i in range(self.capacity)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.capacity

    def addItem(self, key, value):
        hash = self.get_hash(key)
        self.arr[hash] = value

    def getItem(self, key):
        hash = self.get_hash(key)
        return print(self.arr[hash])

    def delete_Item(self, key):
        hash = self.get_hash(key)
        self.arr[hash] = None


h = HashTable()
h.addItem("rahul", 4)
h.addItem("tiwari", 5)
h.addItem("arjun", 6)
h.addItem("pathak", 7)
h.addItem("mohit", 8)
h.addItem("singh", 9)

h.delete_Item("singh")
print(h.arr)


# Hash table working
