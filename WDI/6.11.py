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
    first=Node()
    current=first
    for i in tab:
        temp=Node(i)
        current.next=temp
        current=temp
    return first

def addOrRem(first,val):
    current=first
    previous = first
    czy_dodano=False
    while current is not None:
        if current.val==val:
            previous.next=current.next
            czy_dodano=True
        previous = current
        current = current.next
    if czy_dodano==False:
        previous.next=Node(val)

tab=[9,5,4,2]
lista=make_linked_list(tab)
print_node(lista)
print()
addOrRem(lista,2)
print_node(lista)
print()
addOrRem(lista,1)
print_node(lista)