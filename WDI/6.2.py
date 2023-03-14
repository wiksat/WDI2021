class Node:
    def __init__(self, value = None,zero=None):
        self.val = value
        self.zeros=zero
        self.next = None
def make_linked_list(tab):
    first=Node()
    current=first
    zeros=0
    for i in tab:
        if i!=0:
            temp=Node(i,zeros)
            current.next=temp
            current=temp
            zeros = 0
        else:
            zeros+=1
    if zeros>0:
        temp = Node(0,zeros-1)
        current.next = temp
        current = temp
    return first
def print_node(first):
    current=first.next
    while current is not None:
        print("(",current.zeros,")",current.val,"-->", end="")
        current=current.next

def print_el(first,index):
    current = first.next
    licznik=0
    while current.next is not None:
        if current.zeros>0:
            licznik=licznik+current.zeros
        if licznik>index:
            return 0
        if licznik==index:
            return current.val
        else:licznik+=1
        current=current.next
def podstaw(first,index,value):
    current = first.next
    licznik=0
    while current.next is not None:
        if current.zeros>0:
            licznik=licznik+current.zeros
        if licznik>index:
            print(current.zeros,index,licznik-index,current.zeros-index)
            temp = Node(value, licznik-index)
            current.next.zeros=current.zeros-index
            temp.next=current.next
            current.next=temp
            break
        if licznik==index:
            current.val=value
            break
        else:licznik+=1
        current=current.next
tab=[1,0,0,0,0,3,0,0,5,7,0,0,0,0,4,5,0,0,2,0,0,0,5,0,0,3,3,0,0,0,0]
lista=make_linked_list(tab)
print_node(lista)
print()
print(print_el(lista,3))
podstaw(lista,1,2)
print_node(lista)