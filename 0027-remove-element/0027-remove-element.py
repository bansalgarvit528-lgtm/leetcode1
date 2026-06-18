class Solution(object):
    def removeElement(self, nums, val):
     for i  in range(len(nums)):
        i=0
        while i<len(nums):
            if (nums[i]==val):
                nums.pop(i)
            else:
                i+=1
        print(nums)            