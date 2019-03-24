class Listnode:
    """Listnode represents a node of a linked list. 
    .data contains the value of the node and .next
    contains the address of next node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def search_list(L, key):
    while L and L.val != key:
        L = L.next
    return L


def print_format(L):
    while True:
        print(L.val)
        if L.next is None:
            break
        L = L.next


def insert_after(L, new_L):
    new_L.next = L.next
    L.next = new_L


def delete_after(L):
    L.next = L.next.next

yo = Listnode(21)
# print(yo.val)
bo = Listnode(23)
so = Listnode(4)
insert_after(yo, bo)
insert_after(bo, so)
ans = search_list(yo, 23)
# print(ans.val)
print_format(yo)
delete_after(yo)
print("=====")
print_format(yo)
