# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @param head, a ListNode
# @return a ListNode
def deleteDuplicates(head):
    if head == None:
        return None
    p = head
    while p.next != None:
        if p.val == p.next.val:
            p.next = p.next.next
        else:
            p = p.next
    return head



def printNodes(head):
    p = head
    ans = []
    while p != None:
        ans.append(p.val)
        p = p.next
    print ans

a1 = ListNode(1)
a2 = ListNode(1)
a3 = ListNode(2)
a4 = ListNode(3)
a5 = ListNode(3)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

