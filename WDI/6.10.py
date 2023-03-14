class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None


def print_node(first):
    current = first.next
    while current is not None:
        print(current.val, "-->", end="")
        current = current.next


def make_linked_list(tab):
    first = Node()
    current = first
    for i in tab:
        temp = Node(i)
        current.next = temp
        current = temp
    return first


def dod(first1, first2):
    current1 = first1.next
    current2 = first2.next
    new_list = Node()
    new_current = new_list
    przen = 0
    while current1.next is not None and current2.next is not None:
        new_digit = current1.val + current2.val + przen
        przen = 0
        if new_digit > 9:
            przen = 1
            new_digit -= 10
        temp = Node(new_digit)
        new_current.next = temp
        new_current = temp
        current1 = current1.next
        current2 = current2.next
    # if current1.next is None and current2.next is None:
    new_digit = current1.val + current2.val + przen
    przen = 0
    if new_digit > 9:
        przen = 1
        new_digit -= 10
    temp = Node(new_digit)
    new_current.next = temp
    new_current = temp
    while current1.next is not None:
        new_digit = current1.val + przen
        print(przen,new_digit)
        przen = 0
        if new_digit > 9:
            przen = 1
            new_digit -= 10
        temp = Node(new_digit)
        new_current.next = temp
        new_current = temp
        current1=current1.next
    while current2.next is not None:
        new_digit =  current2.val + przen
        przen = 0
        if new_digit > 9:
            przen = 1
            new_digit -= 10
        temp = Node(new_digit)
        new_current.next = temp
        new_current = temp
        current2=current2.next
    if przen == 1:
        temp = Node(1)
        new_current.next = temp
        # new_current = temp
    return new_list


tab = [1, 2, 3, 4,5]
tab2 = [5, 6, 7, 8]
lista = make_linked_list(tab)
print_node(lista)
print()
lista2 = make_linked_list(tab2)
print_node(lista2)
print()
new = dod(lista, lista2)
print()
print_node(new)
