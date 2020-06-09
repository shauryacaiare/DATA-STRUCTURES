class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.size=0
    def insertstart(self, data):
        self.size += 1
        cur_node = self.head
        newnode = Node(data)
        newnode.next = self.head
        if self.head is None:
            newnode.next = newnode
        else:
            while cur_node.next is not self.head:
                cur_node = cur_node.next
            cur_node.next = newnode
        self.head = newnode

    def insertend(self, data):
        self.size += 1
        newnode = Node(data)
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            curnode = self.head
            while curnode.next is not self.head:
                curnode = curnode.next
            curnode.next = newnode
            newnode.next = self.head
    def insert_between(self,data,data1):
        previousnode=self.head

        if previousnode is None:
            return
        while previousnode.data !=data:
            previousnode=previousnode.next
        newnode=Node(data1)
        newnode.next=previousnode.next
        previousnode.next=newnode


    def traverse(self):
        cur_node=self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next
            if cur_node is self.head:
                break

    def checksize(self):
        return self.size

l=Linkedlist()
l.insertstart("A")
l.insertend("B")
l.insertend("C")
l.insertend("D")
l.insert_between("A",5)
l.traverse()


