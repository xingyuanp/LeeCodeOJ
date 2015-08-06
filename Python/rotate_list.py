# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if head == None:
            return 
        p = q = head
        n = 1
        while k > 0:
            if q.next != None:
                q = q.next
                n += 1
                k -= 1
            else:
                q = head
                k = (k - 1) % n
        while q.next != None:
            p, q = p.next, q.next
        q.next = head
        result = p.next
        p.next = None
        return result