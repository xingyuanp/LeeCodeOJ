class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        x1 = abs(A - C)
        y1 = abs(B - D)
        area1 = x1 * y1
        print area1
        x2 = abs(E - G)
        y2 = abs(F - H)
        area2 = x2 * y2
        print area2
        x3 = min(C, G) - max(A, E)
        y3 = min(D, H) - max(B, F)
        if x3 > 0 and y3 > 0:
            area3 = x3 * y3
        else:
            area3 = 0
        print area3
        return area1 + area2 - area3