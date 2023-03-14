class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None
def print_node(first):
    # current=first.next
    current=first
    while current is not None:
        print("-->",current.val, end="")
        current=current.next
def make_linked_list(tab):
    first=None
    n=len(tab)
    for i in range(n-1,-1,-1):
        tmp=Node(tab[i])
        tmp.next=first
        first=tmp
    return first
def scal(a, b):
    if a == None:
        return b
    if b == None:
        return a
    if a.val < b.val:
        first = a
        first.next = scal(a.next, b)
    else:
        first = b
        first.next = scal(a, b.next)
    return first

tab=[1,4,6,8]
tab2=[5,6,7,8]
lista=make_linked_list(tab)
lista2=make_linked_list(tab2)
print_node(lista)
print()
print_node(lista2)
print()
listaS=scal(lista,lista2)
print_node(listaS)