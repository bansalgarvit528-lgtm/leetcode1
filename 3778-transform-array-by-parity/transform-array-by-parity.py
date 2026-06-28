class Solution(object):
    def transformArray(self, nums):
        result = []

        for num in nums:
            if num % 2 == 0:
                result.append(0)
            else:
                result.append(1)

        result.sort()
        return result