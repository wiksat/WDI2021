class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None
def print_node(first):
    current=first
    while current is not None:
        print(current.val,"-->", end="")
        current=current.next
def make_linked_list(tab):
    first = None
    n = len(tab)
    for i in range(n - 1, -1, -1):
        tmp = Node(tab[i])
        tmp.next = first
        first = tmp
    # guard=Node()
    # guard.next=first
    # first=guard
    return first

def delSmallerThanPrevious(first):
    if first.next is None:
        return first
    current=first.next
    previous = first
    memory=previous.val
    while current.next is not None:
        if current.val<memory:
            previous.next=current.next
            memory=current.val
            current=current.next
        else:
            memory=current.val
            current=current.next
            previous=previous.next
tab=[2,3,4,5,7,9,3,6,8]
lista=make_linked_list(tab)
print_node(lista)
print()
delSmallerThanPrevious(lista)
print_node(lista)