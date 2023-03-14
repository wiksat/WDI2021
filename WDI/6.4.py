from helper_module import *
def make_linked_list(tab):
    first=Node(tab[0])
    current=first
    for i in range(1,len(tab)):
        temp=Node(tab[i])
        current.next=temp
        current=temp
    return first
def reverse(first):
    if first.next is None:
        # return first
        pass
    p=None
    q=first
    r=first.next
    while r is not None:
        q.next=p
        p=q
        q=r
        r=r.next
    q.next=p
    return q
tab=[0,1,2,3,4,5,3,5]
lista=make_linked_list(tab)
print_node(lista)
print()
lista=reverse(lista)
print_node(lista)