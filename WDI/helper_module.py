class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None
def print_node(first):
    current=first
    while current is not None:
        print(current.val,"-->", end="")
        current=current.next
    print()
def make_linked_list(tab):
    first=Node()
    current=first
    for i in tab:
        temp=Node(i)
        current.next=temp
        current=temp
    return first

def make_dual_linkedlist(tab):
    first = Node()
    current = first
    for i in tab:
        current.next = Node(i)
        current.next.prev=current
        current=current.next
    return first

class NodeD:
    def __init__(self, value = None):
        self.val = value
        self.next = None
        self.prev= None