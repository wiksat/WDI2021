class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def przetworz(first):
    firsty = [None for _ in range(10)]
    lasty = [None for _ in range(10)]

    p = first
    while p != None:
        ost = p.val % 10
        if firsty[ost] == None:
            firsty[ost] = lasty[ost] = p
        else:
            lasty[ost].next = p
            lasty[ost] = p

        p = p.next
    result = None
    for i in range(9, -1, -1):
        if firsty[i] != None:
            lasty[i].next = result
            result = firsty[i]
    return result
