from helper_module import *

def isEvenOnesNumberInBinary(number):
    ones = 0
    while number > 0:
        w = number % 2
        number //= 2
        if w == 1:
            ones += 1
    print(ones%2==0)
    return ones%2==0
def delFromDualLinkedlist(first):
    previous=first
    current=first.next
    while current.next is not None:
        if isEvenOnesNumberInBinary(current.val):
            previous.next=current.next
            current.next.prev=previous
            current = current.next
        else:
            previous = previous.next
            current = current.next
    # print(current.prev.val,current.val)
    if isEvenOnesNumberInBinary(current.val):
        current.prev.next=None

tab=[0,1,2,3,4,5]
lista=make_dual_linkedlist(tab)
print_node(lista)
print()
delFromDualLinkedlist(lista)
print_node(lista)