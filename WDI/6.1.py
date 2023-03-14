class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None
class zbior:
    def __init__(self):
        self.first=Node()
    def find(self,val):
        current=self.first
        while current.val != val and current.next is not None:
            current=current.next
        return current.val == val
    def add(self,val):
        if not zbior.find(self,val):
            current=self.first
            while current.next is not None:
                current=current.next
            current.next=Node(val)
    def delete(self,val):
        current = self.first
        previous = self.first
        while current.val != val and current.next is not None:
            previous=current
            current=current.next
        if current.val!=val:
            return False
        else:
            current.val=None
            previous.next=current.next
lista = zbior()
# print(lista)
lista.add(12)
lista.add(13)
lista.add(2)
print(lista.find(13))
lista.delete(13)
print(lista.find(13))
print(lista.find(2))