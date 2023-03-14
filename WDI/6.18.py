from helper_module import *
def unikal(first):
    current=first
    previous=first
    if current.val is None:
        current = current.next
    while current is not None:
        if ile(first,current.val)>1:
            previous.next=current.next
            current_usun=current.next
            previuos_usun=previous
            while current_usun is not None:
                print(current_usun.val)
                if current_usun.val==current.val:
                    print("przeszlo")
                    previuos_usun.next=current_usun.next
                    current_usun=current_usun.next
                else:
                    previuos_usun=previuos_usun.next
                    current_usun=current_usun.next
            current=current.next
        else:
            previous=previous.next
            current=current.next

def ile(first,val):
    current=first
    ile=0
    while current is not None:
        if current.val==val:
            ile+=1
        current=current.next
    return ile
tab=[0,1,2,3,4,5,3,5]
lista=make_linked_list(tab)
print_node(lista)
print()
unikal(lista)
print_node(lista)