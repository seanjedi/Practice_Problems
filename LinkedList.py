class node:
    def __init__(self, data = None):
        self.__data = data
        self.__next = None
    def getData(self):
        return self.__data
    def setData(self, data):
        self.__data = data
    def getNext(self):
        return self.__next
    def setNext(self, next):
        self.__next = next


class linkedList:
    def __init__(self, data = None):
        self.__head = node(data)
    
    def insert(self, data):
        cur = self.__head
        if(self.__head.getData() is None):
            self.__head.setData(data)
        while(cur.getNext() is not None):
            cur = cur.getNext()
        cur.setNext(node(data))
    
    def search(self, data):
        cur = self.__head
        while(cur is not None):
            if(cur.getData() is data):
                print("Found: ", data)
                return True
            cur = cur.getNext()
        print(data, "Not Found!")
        return False
    
    def print(self):
        cur = self.__head
        print("This is the list:")
        while(cur is not None):
            print("\tNode Value: ", cur.getData())
            cur = cur.getNext()
        print("\n")
        
    def kFromLast(self, k):
        pos = abs(k)
        loc = None
        cur = self.__head
        while cur is not None:
            if pos is not 0:
                pos -= 1
            else:
                if loc is None:
                    loc = self.__head
                else:
                    loc = loc.getNext()
            cur = cur.getNext()
        if loc is None:
            print("K is outside Range!")
            return False
        else:
            print("k from the last is: ", loc.getData())
            return True


    def printBackwards(self):
        cur = self.__head
        array = []
        print("This is the list backwards:")
        while(cur is not None):
            array.append(cur.getData())
            cur = cur.getNext()
        while(len(array) is not 0):
            print("\tNode Value: ", array.pop())
        print("\n")
    
    def remove(self, data):
        cur = self.__head
        if cur is None:
            print("List has no Items!")
            return False
        if cur.getData() is data:
            if cur.getNext() is not None:
                self.__head = cur.getNext()
            print("Removed Item: ", data)
            del cur
            return True
        
        prev = cur
        cur = cur.getNext()
        while cur is not None:
            if cur.getData() is data:
                prev.setNext(cur.getNext())
                del cur
                print("Removed Item: ", data)
                return True
            prev = cur
            cur = cur.getNext()
        print("Can't remove what doesn't exist!")

llist = linkedList(1)
llist.insert(2)
llist.insert(5)
llist.insert(4)
llist.insert(3)
llist.insert(10)
llist.insert(11)
llist.insert(8)

llist.search(10)
llist.remove(10)
llist.search(10)
llist.print()
llist.printBackwards()
llist.kFromLast(-3)