class Solution(object):
    def countPartitions(self, nums):
        count = 0

        for i in range(len(nums) - 1):
            left = sum(nums[:i + 1])
            right = sum(nums[i + 1:])

            if (left - right) % 2 == 0:
                count += 1

        return count