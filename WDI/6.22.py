class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None
def print_node(first):
    current=first.next
    while current is not None:
        print(current.val,"-->", end="")
        current=current.next
def make_linked_list(tab):
    first=Node()
    # first = Node(tab[0])
    current=first
    # for i in range(1,len(tab)):
    for i in tab:
        # temp=Node(tab[i])
        temp = Node(i)
        current.next=temp
        current=temp
    return first
def is_Cycle(first):
    one_step=first
    two_step=first
    if two_step.next is not None and two_step.next.next is not None:
        one_step=one_step.next
        two_step=two_step.next.next
        while one_step.next is not None and two_step.next is not None and  two_step.next.next is not None:
            if one_step==two_step:
                return True
            one_step = one_step.next
            two_step = two_step.next.next
    return False
tab=[9,9]
lista=make_linked_list(tab)

print_node(lista)
# lista.next.next=lista.next
print()
print(is_Cycle(lista))
lista.next.next=lista.next
print()
print(is_Cycle(lista))