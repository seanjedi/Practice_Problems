class node:
    "this is a node"
    def __init__(self, data = None, left = None, right = None):
        self.__data = data
        self.__left = left
        self.__right = right
    def getRight(self):
        return self.__right
    
    def setRight(self, right):
        self.__right = right
    
    def getLeft(self):
        return self.__left
    
    def setLeft(self, left):
        self.__left = left

    def getData(self):
        return self.__data
    
    def setData(self, data):
        self.__data = data

class doubleLinkedList:
    "this is a double linked list"
    def __init__(self, data = None):
        self.__head = node(data)
    
    def insert(self, data):
        if(self.__head.getData() is None):
            self.__head.setData(data)
            return
        cur = self.__head
        while(cur.getRight() != None):
            cur = cur.getRight()
        new = node(data, cur)
        cur.setRight(new)

    def search(self, data):
        cur = self.__head
        while(cur is not None):
            if(cur.getData() is data):
                return True
            cur = cur.getRight()
        return False
    
    def remove(self, data):
        cur = self.__head
        while(cur is not None):
            if(cur.getData() is data):
                left = cur.getLeft()
                right = cur.getRight()
                left.setRight(right)
                right.setLeft(left)
                print("removed: ", data)
                del cur
                return True
            cur = cur.getRight()
        print("Cant remove what doesnt exist!")
        return False

    def print(self):
        print("The list values are: ")
        cur = self._doubleLinkedList__head
        while(cur is not None):
            print("\tNode Value: ", cur.getData())
            cur = cur.getRight()
        print ("\n")
        
    def printBackwards(self):
        print("The list values backwards are: ")
        cur = self._doubleLinkedList__head
        while(cur.getRight() is not None):
            cur = cur.getRight()
        while(cur is not None):
            print("\tNode Value: ", cur.getData())
            cur = cur.getLeft()
        print("\n")

llist = doubleLinkedList(1)
llist.insert(5)
llist.insert(3)
llist.insert(4)
llist.insert(6)
llist.print()

llist.remove(5)
llist.remove(-1)
llist.printBackwards()

llist.print()