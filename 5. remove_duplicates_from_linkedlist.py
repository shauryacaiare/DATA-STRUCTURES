class Node:
    def __init__(self,data):
        self.data=data
        self.nextnode=None

class linkedlist:
    def __init__(self):
        self.head=None
        self.size=0
    def insertstart(self,data):
        self.size+=1
        newnode=Node(data)

        if self.head is None:
            self.head=newnode
        else:
            newnode.nextnode=self.head
            self.head=newnode
    def insertend(self,data):
        self.size+=1
        newnode=Node(data)

        if self.head is None:
            self.head=newnode
        else:
            actualnode=self.head
            while actualnode.nextnode is not None:
                actualnode=actualnode.nextnode
            actualnode.nextnode=newnode
    def insert_between(self,data,data1):
        previousnode=self.head

        if previousnode is None:
            return
        while previousnode.data !=data:
            previousnode=previousnode.nextnode
        newnode=Node(data1)
        newnode.nextnode=previousnode.nextnod
        previousnode.nextnode=newnode

    def remove_duplicates(self,list):
        dict1={}
        currentnode=self.head
        previousnode=None
        while currentnode is not None:
            if currentnode.data not in dict1:
                dict1[currentnode.data]=1
                previousnode=currentnode
                currentnode = currentnode.nextnode

            else:
                previousnode.nextnode=currentnode.nextnode
                currentnode = currentnode.nextnode



    def traverse(self):

        currentnode=self.head
        while currentnode is not None:
            print(currentnode.data)
            currentnode=currentnode.nextnode

l=linkedlist()
l.insertstart(1)
l.insertend(2)
l.insertend(2)
l.insertend(4)
l.insertend(4)
l.insertend(8)
l.remove_duplicates(l)
l.traverse()
