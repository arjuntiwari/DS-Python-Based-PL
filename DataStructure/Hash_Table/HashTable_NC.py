class HashTable:
    def __init__(self):
        self.capacity = 10
        self.arr = [[] for i in range(self.capacity)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.capacity

    def addItem(self, key, value):
        hash = self.get_hash(key)
        found = False
        for id, element in enumerate(self.arr[hash]):
            if element[0] == key and len(element) == 2:
                self.arr[hash][id] = (key, value)
                found = True
                break
        if not found:
            self.arr[hash].append((key, value))

    def getItem(self, key):
        hash = self.get_hash(key)
        for element in self.arr[hash]:
            if element[0] == key:
                return print(element[1])

        print("Not Exists")

    def delete_Item(self, key):
        hash = self.get_hash(key)
        self.arr[hash] = None

    def print_items(self):
        for element in enumerate(self.arr):
            print(element)


h = HashTable()
h.addItem("rahul", 4)
h.addItem("tiwari", 5)
h.addItem("arjun", 6)
h.addItem("ret", 12)
h.addItem("pet", 13)
h.addItem("set", 14)
h.addItem("jet", 7)
h.addItem("pathak", 10)
h.addItem("mohit", 8)
h.addItem("singh", 9)
h.getItem("ret")


h.print_items()


# liner probing & Non collision in hash table
