from helper_module import *
def isEvenFivesNumberInOctal(number):
    fives = 0
    while number > 0:
        w = number % 8
        number //= 8
        if w == 5:
            fives += 1
    return fives%2==0
def toFront(first):
    current = first
    previous = first
    if current.val is None:
        current = current.next
    while current is not None:
        if isEvenFivesNumberInOctal(current.val)and first.next!=current:
            wskazanie_wartownika=first.next
            wskazanie_nastepcy_obecnego_elementu=current.next
            first.next=current
            current.next=wskazanie_wartownika
            previous.next = wskazanie_nastepcy_obecnego_elementu
            current = wskazanie_nastepcy_obecnego_elementu
        else:
            current=current.next
            previous=previous.next


tab=[0,1,2,3,4,5]
lista=make_linked_list(tab)
print_node(lista)
print()
toFront(lista)
print_node(lista)
