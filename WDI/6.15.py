from helper_module import *
def isMoreOneThanTwoInTricimal(number):
    one=0
    two=0
    while number>0:
        w=number%3
        number//=3
        if w==1:
            one+=1
        elif w==2:
            two+=1
    return one>two
def delMoreOneThanTwo(first):
    current=first
    previous=first
    if current.val is None:
        current = current.next
    while current is not None:
        if isMoreOneThanTwoInTricimal(current.val):
            previous.next=current.next
            current = current.next
        else:
            previous=previous.next
            current=current.next

tab=[0,1,2,3,4,1]
lista=make_linked_list(tab)
print_node(lista)
print()
delMoreOneThanTwo(lista)
print_node(lista)