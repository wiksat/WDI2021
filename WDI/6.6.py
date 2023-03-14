class Node:
    def __init__(self,value=None):
        self.val=value
        self.next=None
def push_back(head,val):
    curr=head
    while curr.next is not None:
        curr=curr.next
    curr.next=Node(val)
def print_node(first):
    current=first.next
    while current is not None:
        print(current.val,"-->", end="")
        current=current.next
def make_linked_list(tab):
    first=Node()
    current=first
    for i in tab:
        temp=Node(i)
        current.next=temp
        current=temp
    return first

tab=[9,9,9,9]
lista=make_linked_list(tab)
print_node(lista)
print()
push_back(lista,5)
print_node(lista)