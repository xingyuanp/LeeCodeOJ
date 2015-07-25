class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        ds, dt = {}, {}
        for cs, ct in zip(s, t):
            if cs not in ds and ct not in dt:
                ds[cs], dt[ct] = ct, cs
            elif cs in ds and ct not in dt:
                return False
            elif cs not in ds and ct in dt:
                return False
            elif ds[cs] != ct:
                return False
        return True