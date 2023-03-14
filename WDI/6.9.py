class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None
def print_node(first):
    current=first.next
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
def dod(first):
    current=first.next
    current.val+=1
    while current.val>9:
        current.val=0
        if current.next is not None:
            current=current.next
            current.val+=1
        else:
            current.next=Node(1)
            current=current.next
tab=[9,9,9,9]
lista=make_linked_list(tab)
print_node(lista)
print()
dod(lista)
print_node(lista)