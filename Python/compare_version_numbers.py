class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        if len(v1) < len(v2):
            v1 = v1 + ['0'] * (len(v2) - len(v1))
        else:
            v2 = v2 + ['0'] * (len(v1) - len(v2))       
        for i in range(len(v1)):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1
        return 0