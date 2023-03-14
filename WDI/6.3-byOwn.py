class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
def print_node(first):
    # current=first.next
    current=first
    while current is not None:
        print("-->",current.value, end="")
        current=current.next
def make_linked_list(tab):
    first=None
    n=len(tab)
    for i in range(n-1,-1,-1):
        tmp=Node(tab[i])
        tmp.next=first
        first=tmp
    return first
def scal(a,b):
    if a.value<b.value:
        new=a
        a=a.next
    else:
        new=b
        b=b.next
    first=new
    while a is not None and b is not None:
        if a.value<b.value:
            new.next=a
            a=a.next
        else:
            new.next=b
            b=b.next
        new=new.next
    if a is None:
        new.next=b
    else:
        new.next=a
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