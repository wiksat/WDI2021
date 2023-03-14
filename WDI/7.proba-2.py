class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None
def print_node(first):
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
def iloczyn(l1,l2,l3):
    if l1 is None or l2 is None or l3 is None:
        return None
    new=Node()
    zwrot=new
    while l1 is not None and l2 is not None:
        if l1.val>l2.val:
            l2=l2.next
        elif l1.val<l2.val:
            l1=l1.next
        elif l1.val==l2.val:
            while l3 is not None and l3.val<l1.val:
                l3=l3.next
            if l3.val is not None and l3.val==l1.val:
                new.next=l3
                new=new.next
                q = l3.next
                new.next=None
                l3=q
            l1 = l1.next
            l2 = l2.next
    return zwrot.next


tab=[1,4,6,9]
tab2=[5,6,7,9]
tab3=[6,9,10,11]
lista=make_linked_list(tab)
lista2=make_linked_list(tab2)
lista3=make_linked_list(tab3)
print_node(lista)
print()
print_node(lista2)
print()
print_node(lista3)
print()
print()
# print_node(oblicz(lista,lista2))
print_node(iloczyn(lista,lista2,lista3))