class Solution(object):
    def totalMoney(self, n):
        money = 0
        start = 1

        while n > 0:
            for i in range(7):
                if n == 0:
                    break
                money += start + i
                n -= 1
            start += 1

        return money