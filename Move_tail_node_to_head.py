class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.size=0
    def insertstart(self,data):
        self.size+=1
        newnode=Node(data)

        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def insertend(self,data):
        self.size+=1
        actualnode=self.head
        newnode=Node(data)
        while actualnode.next is not None:
            actualnode=actualnode.next
        actualnode.next=newnode
    def tail_to_head(self):
        endnode=self.head
        pre1_node=None
        while endnode and endnode.next:
            pre1_node=endnode
            endnode=endnode.next

        endnode.next=self.head
        self.head=endnode
        pre1_node.next=None
    def traverse(self):
        cur_node=self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node=cur_node.next

l=Linkedlist()
l.insertstart("A")
l.insertend("B")
l.insertend("C")
l.insertend("D")
l.tail_to_head()
l.traverse()

