class Node:
    "This is a data node for the Binary Tree"
    def __init__(self, Data = None, left = None, right = None):
        self.__data = Data
        self.__leftNode = left
        self.__rightNode = right

    def setRight(self, right):
        self.__rightNode = right

    def setLeft(self, left):
        self.__leftNode = left
    
    def getRight(self):
        return self.__rightNode

    def getLeft(self):
        return self.__leftNode
    def setData(self, data = None):
        self.__data = data
    def getData(self):
        return self.__data

    def __del__(self):
        if(self.__rightNode):
            del self.__rightNode
        if(self.__leftNode):
            del self.__leftNode

class binaryTree:
    "This is my implementation of a binary tree"
    def __init__(self, data = None):
        self.head = Node(data)
    
    def insert(self, data):
        if self.head.getData() is None:
            self.head.setData(data)
            return
        else:
            cur = self.head

        while(cur is not None):
            if(data <= cur.getData()):
                if(cur.getLeft()):
                    cur = cur.getLeft()
                else:
                    newNode = Node(data)
                    cur.setLeft(newNode)
                    cur = None
            elif(data > cur.getData()):
                if(cur.getRight()):
                    cur = cur.getRight()
                else:
                    newNode = Node(data)
                    cur.setRight(newNode)
                    cur = None
    
    def search(self, data):
        if self.head is None:
            return False
        else:
            cur = self.head
        while cur is not None:
            if(cur.getData() == data):
                return True
            if(data <= cur.getData()):
                cur = cur.getLeft()
            else:
                cur = cur.getRight()
        return False
    
    def inOrderPrint(self):
        cur = self.head
        stack = []
        done = 0
        while not done:
            if cur is not None:
                stack.append(cur)
                cur = cur.getLeft()
            else:
                if len(stack) > 0:
                    cur = stack.pop()
                    print(cur.getData())
                    cur = cur.getRight()
                else:
                    done = 1

    def preOrderPrint(self):
        cur = self.head
        stack = []
        done = 0
        while not done:
            if cur is not None:
                print(cur.getData())
                stack.append(cur)
                cur = cur.getLeft()
            else:
                if len(stack) > 0:
                    cur = stack.pop()
                    cur = cur.getRight()
                else:
                    done = 1

    def postOrderPrint(self):
        cur = self.head
        stack = []
        done = 0
        while not done:
            if cur is not None:
                stack.append(cur)
                cur = cur.getRight()
            else:
                if len(stack) > 0:
                    cur = stack.pop()
                    print(cur.getData())
                    cur = cur.getLeft()
                else:
                    done = 1

    
    def __del__(self):
        if self.head is not None:
            del self.head

# Tree = binaryTree()
# Tree.insert(10)
# Tree.insert(5)
# Tree.insert(4)
# Tree.insert(6)
# Tree.insert(15)
# Tree.insert(13)
# Tree.insert(20)

# # print(Tree.search(9))
# Tree.postOrderPrint()
# del Tree

llist = binaryTree(5)
llist.insert(3)
llist.insert(2)
llist.insert(0)
llist.insert(1)
llist.insert(6)
llist.insert(7)
llist.insert(5)
llist.inOrderPrint()