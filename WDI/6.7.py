def del_last(first):
    previous=first
    current=first
    while current.next is not None:
        previous=current
        current=current.next
    previous.next=None