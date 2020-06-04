class Node:
    def __init__(self, data):
        self.data = data
        self.nextnode = None


class linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertstart(self, data):
        self.size += 1
        newnode = Node(data)


        if not self.head:
            self.head = newnode
        else:
            newnode.nextnode = self.head
            self.head = newnode

    def insertend(self, data):
        newnode = Node(data)
        self.size += 1
        actualnode = self.head

        while actualnode.nextnode is not None:
            actualnode = actualnode.nextnode
        actualnode.nextnode = newnode

    def traverse(self):

        currentnode=self.head
        while currentnode is not None:
            print(currentnode.data)
            currentnode=currentnode.nextnode

    def mergelist(self,lk2):
        p=self.head
        q=lk2.head
        if p is None:
            return q
        if not q:
            return p
        s=None
        if p and q:
            if p.data<q.data:
                s=p
                p=s.nextnode
            else:
                s=q
                q=s.nextnode
        new_head=s
        while p and q:
            if p.data<=q.data:
                s.nextnode=p
                s=p
                p=s.nextnode
            else:
                s.nextnode=q
                s=q
                q=s.nextnode
        if q is None:
            s.nextnode=p
        if p is None:
            s.nextnode=q

lk1=linkedlist()
lk1.insertstart(1)
lk1.insertend(5)
lk1.insertend(7)
lk1.insertend(9)
lk1.insertend(10)

lk2=linkedlist()

lk2.insertstart(2)
lk2.insertend(3)
lk2.insertend(4)
lk2.insertend(6)
lk2.insertend(8)
lk1.traverse()
print("-"*100)
lk2.traverse()
lk1.mergelist(lk2)
print("-"*100)
lk1.traverse()
















