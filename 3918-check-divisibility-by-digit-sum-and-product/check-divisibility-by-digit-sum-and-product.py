class Solution:
    def checkDivisibility(self, n):
        x = n
        sum = 0
        product = 1

        while x > 0:
            digit = x % 10
            sum = sum + digit
            product = product * digit
            x = x // 10

        if n % (sum + product) == 0:
            return True
        else:
            return False