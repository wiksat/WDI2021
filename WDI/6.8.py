class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None

def del_every_second(first):
    current=first
    previous=first
    f=False
    while current.next is not None:
        previous = current
        current = current.next
        f=not f
        if f:
            # print("dzia")
            current.val = None
            previous.next = current.next


def print_node(first):
    current=first
    while current is not None:
        print(current.val,"-->", end="")
        current=current.next
def make_linked_list(tab):
    first=Node()
    current=first
    for i in tab:
        temp=Node(i)
        current.next=temp
        current=temp
    return first


tab=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
lista=make_linked_list(tab)
print_node(lista)
print()
del_every_second(lista)
print_node(lista)