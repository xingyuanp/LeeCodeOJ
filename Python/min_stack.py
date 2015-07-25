class MinStack:
    def __init__(self):
        self.v = []    
    
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if self.v == [] or x < self.getMin():
            self.v.append((x, x))
        else:
            self.v.append((x, self.getMin()))
        return x
        
    # @return nothing
    def pop(self):
        self.v.pop()
        
    # @return an integer
    def top(self):
        return self.v[-1][0]

    # @return an integer
    def getMin(self):
        return self.v[-1][1]
        