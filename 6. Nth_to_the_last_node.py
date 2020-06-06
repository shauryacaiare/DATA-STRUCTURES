""""in this code  if the linked list is 1->2->3->4->5 and value of n is 2 in the function than the output will be 4 as 4 is 2nd node
       from the last node"""

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
        self.size+=1
        newnode=Node(data1)
        newnode.nextnode=previousnode.nextnode
        previousnode.nextnode=newnode
    def nth_to_last_node(self,n):
        size=self.checksize()
        index_node_to_find=size-n+1
        s=0
        currentnode=self.head
        while currentnode is not None:
            s+=1
            if s!=index_node_to_find:
                currentnode=currentnode.nextnode
            else:
                return currentnode.data

    def traverse(self):

        currentnode = self.head
        while currentnode is not None:
            print(currentnode.data)
            currentnode = currentnode.nextnode

    def checksize(self):
        return self.size

l=linkedlist()
l.insertstart(1)
l.insertend(2)
l.insertend(3)
l.insertend(4)
l.insertend(5)
l.traverse()
print("-"*100)
print(l.nth_to_last_node(4))
