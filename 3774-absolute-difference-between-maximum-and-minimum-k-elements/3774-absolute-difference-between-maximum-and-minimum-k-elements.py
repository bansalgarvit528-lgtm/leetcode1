class Solution(object):
    def absDifference(self, nums, k):
        nums.sort()

        a = sum(nums[:k])      # Sum of smallest k elements
        b = sum(nums[-k:])     # Sum of largest k elements

        return abs(b - a)