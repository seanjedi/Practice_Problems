import random
import copy
import time
random.seed(200)

class Node:
    "This is a data node for the linkedList"
    def __init__(self, Key = None, Data = None):
        self.__data = Data
        self.__key = Key
        self.__next = None

    def setNext(self, Next):
        self.__next = Next
    
    def getNext(self):
        return self.__next

    def getData(self):
        return self.__data
    
    def getKey(self):
        return self.__key

    def __del__(self):
        if(self.__next):
            del self.__next

class hashTable:
    "This is my implementation of a hashTable with a Linked List"
    def __init__(self, Size = 1, Limit = 0.8):
        if Size <= 0:
            Size = 1
        self.__maxSize = Size
        self.__curSize = 0
        self.__limit = Limit
        self.table = [None] * Size
        # self.hashValue = int(random.random() * 1000)
        self.hashValue = Size
    
# Hash Function
    def hash(self, key):
        hash = key % self.hashValue
        return hash
    
#Rehash Function 
    def reHash(self):
        self.__maxSize *= 2
        if self.__hashValue < self.maxSize:
            self.__hashValue = self.maxSize
        newTable = hashTable(self.__maxSize)
        for cur in self.table:
            while cur is not None:
                newTable.insert(cur.getKey(), cur.getData())
                cur = cur.getNext()
        self.table = copy.deepcopy(newTable.table)
        del newTable

# Insert Function
    def insert(self, key, data):
        if(self.__curSize >= int(self.__maxSize * self.__limit)):
            self.reHash()
        pos = hash(key)%self.__maxSize
        cur = self.table[pos]
        self.__curSize += 1
        if cur is None:
            self.table[pos] = Node(key, data)
            return
        while cur is not None:
            prev = cur
            cur = cur.getNext()
        prev.setNext(Node(key, data))

# Insert No Re-Hash Function
#A function to test my linked list implementation by checking what happens if it never rehashes
    def insertNoHash(self, key, data):
        pos = hash(key)%self.__maxSize
        cur = self.table[pos]
        self.__curSize += 1
        if cur is None:
            self.table[pos] = Node(key, data)
            return
        while cur is not None:
            prev = cur
            cur = cur.getNext()
        prev.setNext(Node(key, data))
    
# Search Function 
    def search(self, key):
        pos = hash(key)%self.__maxSize
        if self.table[pos] is None:
            return False
        cur = self.table[pos]       
        while cur is not None:
            if cur.getKey() == key:
                return cur.getData()
            else:
                cur = cur.getNext()
        return False

# Delete Function
    def __del__(self):
        for i in self.table:
            if i is not None:
                del i

Table = hashTable()
Table.insert(1, 2)
Table.insert(2, 2)
Table.insert(3, 3)
Table.insert(3, 3)
Table.insert(4, 4)
Table.insert(10, 123)
Table.insert(200, 321)
Table.insert(21, 83)

start = time.time()
for i in range (20000):
    data = int(random.random() * 1000000)
    key = int(random.random() * 1000000)
    Table.insert(key, data)

end = time.time()
print("Time for normal execution:", end - start)

#Test Normal hash function
# print(Table.search(4))
# print(Table.search(2))
# print(Table.search(200))
# print(Table.search(123))

#Test No Hash Functionality
Table2 = hashTable()
Table2.insert(1,2)
Table2.insert(10,123)
start = time.time()
for i in range (20000):
    data = int(random.random() * 1000000)
    key = int(random.random() * 1000000)
    Table2.insertNoHash(key, data)

end = time.time()
print("Time for no rehash execution:", end - start)

# print(Table2.search(1))
# print(Table2.search(10))
# print(Table2.search(123))

del Table