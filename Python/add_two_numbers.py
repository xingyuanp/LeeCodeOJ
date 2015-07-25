# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        s = l1.val + l2.val
        head = ListNode(s % 10)
        remaining = self.addTwoNumbers(l1.next, l2.next)
        if s > 9:
            remaining = self.addTwoNumbers(remaining, ListNode(1))
        head.next = remaining
        return head