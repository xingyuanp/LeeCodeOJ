# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            leftMatch = self.isSameTree(p.left, q.left) 
            rightMatch = self.isSameTree(p.right, q.right)
            return (p.val == q.val) and leftMatch and rightMatch