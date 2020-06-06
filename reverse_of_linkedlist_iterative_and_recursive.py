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
    def traverse(self):

        currentnode=self.headnode
        while currentnode is not None:
            print(currentnode.data)
            currentnode=currentnode.nextnoder

    def reverselist(self):
        pre_node=None
        curr_node=self.headnode

        while curr_node is not None:
            next1 = curr_node.nextnoder
            curr_node.nextnoder = pre_node
            pre_node = curr_node
            curr_node = next1
        self.headnode=pre_node

    def recursive_reverse(self):
        def _recuresive_reverse(cur_node1,pre_node1):
            if cur_node1 is None:
                return pre_node1
            next1 = cur_node1.nextnoder
            cur_node1.nextnoder = pre_node1
            pre_node1 = cur_node1
            cur_node1 = next1
            return _recuresive_reverse(cur_node1,pre_node1)
        self.headnode=_recuresive_reverse(cur_node1=self.headnode,pre_node1=None)

l=linklist()
l.insertstart("A")
l.insertend("B")
l.insertend("C")
l.insertend("D")
l.traverse()
l.reverselist()

print("-"*100)
l.traverse()
l2=linklist()
l2.insertstart("A")
l2.insertend("B")
l2.insertend("C")
l2.insertend("D")
l2.recursive_reverse()
print("-"*100)
l2.traverse()