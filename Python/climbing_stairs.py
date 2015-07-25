class Solution:
    def __init__(self):
        self.c = {}
    
    def climbStairs(self, n):
        if n not in self.c:
            if n == 1 or n == 2:
                self.c[n] = n
            else:
                self.c[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.c[n]   

