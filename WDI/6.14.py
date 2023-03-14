from helper_module import *
def delElMod0Next(first):
    current=first
    previous=first
    if current.val is None:
        current = current.next
    while current.next is not None:
        # print(current.next.val,current.val)
        if current.next.val%current.val==0:
            previous.next=current.next
            current = current.next
        else:
            previous=previous.next
            current=current.next

tab=[2,4,5,7,2,4,8,3,6,8]
lista=make_linked_list(tab)
print_node(lista)
print()
delElMod0Next(lista)
print_node(lista)