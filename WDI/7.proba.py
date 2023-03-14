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
def iloczyn(first1,first2,first3):
    list=oblicz(first1,first2)
    return oblicz(list,first3)
def oblicz(first1,first2):
    if first1 is None:
        return first2
    if first2 is None:
        return first1
    new=None
    if first1.val<first2.val:
        new=first1
        first1=first1.next
    else:
        new = first2
        first2 = first2.next
    zwrot=new
    while first1 is not None and first2 is not None:
        if first1.val < first2.val:
            # print("war1",new.val,first1.val)
            if new.val==first1.val:
                first1 = first1.next
            else:
                new.next = first1
                first1 = first1.next
                new=new.next
        else:
            # print("war2", new.val, first2.val)
            if new.val==first2.val:
                first2 = first2.next
            else:
                new.next = first2
                first2 = first2.next
                new = new.next
    if first2 is None:
        new.next=first1
    if first1 is None:
        new.next=first2
    return zwrot
tab=[1,4,6,8]
tab2=[5,6,7,9]
tab3=[8,9,10,11]
lista=make_linked_list(tab)
lista2=make_linked_list(tab2)
lista3=make_linked_list(tab3)
print_node(lista)
print()
print_node(lista2)
print()
print_node(lista3)
print()
# print_node(oblicz(lista,lista2))
print_node(iloczyn(lista,lista2,lista3))