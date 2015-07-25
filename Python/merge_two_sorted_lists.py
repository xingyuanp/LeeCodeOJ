# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @param two ListNodes
# @return a ListNode
def mergeTwoLists(l1, l2):
    head = ListNode(0)
    current = head
    while l1 != None and l2 != None:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next     
    if l1 == None:
        current.next = l2
    else:
        current.next = l1
    return head.next           








##############################################################################
def printNodes(a):
    t = []
    while a != None:
        t.append(a.val)
        a = a.next
    print t


a1 = ListNode(3)
b1 = ListNode(5)
c1 = ListNode(9)
a1.next = b1
b1.next = c1
l1 = a1

a2 = ListNode(4)
b2 = ListNode(6)
c2 = ListNode(7)
a2.next = b2
b2.next = c2
l2 = a2

