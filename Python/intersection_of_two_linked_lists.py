# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        a_set = set()
        p = headA
        while p != None:
            a_set.add(p)
            p = p.next
        p = headB
        while p != None:
            if p in a_set:
                return p
            p = p.next
        return None