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

    def traverse(self):

        currentnode = self.head
        while currentnode is not None:
            print(currentnode.data)
            currentnode = currentnode.nextnode

    def checksize(self):
        return self.size

    def occurence(self):
        dict1={}
        cur_node=self.head
        while cur_node is not None:
            if cur_node.data not in dict1:
                dict1[cur_node.data]=1
            else:
                dict1[cur_node.data]+=1
            cur_node=cur_node.nextnode
        return dict1

l=linkedlist()
l.insertstart(1)
l.insertend(2)
l.insertend(2)
l.insertend(2)
l.insertend(3)
l.insertend(4)
l.insertend(5)
data=l.occurence()
import pandas as pd
list1=list(data.keys())
list2=list(data.values())
df=pd.DataFrame({"elments":list1,"occurences":list2})
print(df)