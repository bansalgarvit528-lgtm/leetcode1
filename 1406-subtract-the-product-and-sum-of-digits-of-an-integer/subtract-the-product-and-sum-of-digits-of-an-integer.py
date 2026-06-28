class Solution(object):
    def subtractProductAndSum(self, n):
        dsum = 0
        dproduct = 1

        while n > 0:
            digit = n % 10
            dsum += digit
            dproduct *= digit
            n = n // 10
            
        return dproduct - dsum