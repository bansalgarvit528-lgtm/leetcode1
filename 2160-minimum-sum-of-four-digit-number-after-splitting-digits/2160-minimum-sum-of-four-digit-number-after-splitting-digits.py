class Solution:
    def minimumSum(self, num):
        d = list(str(num))
        d.sort()

        return int(d[0] + d[2]) + int(d[1] + d[3])