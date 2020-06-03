class Node:
    def __init__(self,data):
        self.data=data
        self.nextnoder=None

class linklist:
    def __init__(self):
        self.headnode=None
        self.size=0
    #time complexity is O(1) for inserting the data at the starting
    def insertstart(self,data):

        newnode = Node(data)
        self.size+=1 #usefull as we will be able to check to size of the array without loop

        if self.headnode is None:
            self.headnode=newnode
        else:
            newnode.nextnoder=self.headnode
            self.headnode = newnode

    #time complexity is O(N)
    def insertend(self,data):
        newnode=Node(data)
        self.size+=1
        actualnode=self.headnode

        while actualnode.nextnoder is not None:
            actualnode = actualnode.nextnoder
        actualnode.nextnoder=newnode
    def insert_between(self,data,data1):
        previousnode=self.headnode

        if previousnode is None:
            return
        while previousnode.data !=data:
            previousnode=previousnode.nextnoder
        newnode=Node(data1)
        newnode.nextnoder=previousnode.nextnoder
        previousnode.nextnoder=newnode

    def removeel(self,data):
        self.size-=1
        currentnode=self.headnode
        previousnode=None

        if currentnode is None:
            print("linked list is empty")
        while currentnode.data != data:
            previousnode=currentnode
            currentnode=currentnode.nextnoder

        if previousnode is None:
            self.headnode=currentnode.nextnoder
        else:
            previousnode.nextnoder=currentnode.nextnoder

    def traverse(self):

        currentnode=self.headnode
        while currentnode is not None:
            print(currentnode.data)
            currentnode=currentnode.nextnoder

    #time complexity is O(1)
    def checksize(self):
        return self.size
if __name__ == '__main__':
    l=linklist()
    l.insertstart(23)
    l.insertend(45)
    l.insertend(55)
    l.insertend(56)
    l.insertend(78)
    l.traverse()
    print("-"*100)
    l.insert_between(55,79)
    l.traverse()
