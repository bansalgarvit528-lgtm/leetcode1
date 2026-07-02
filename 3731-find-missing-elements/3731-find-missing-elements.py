class Solution(object):
    def findMissingElements(self, nums):
       g=[]
       for i in range(min(nums)+1,max(nums)):
        if i not in nums:
            g.append(i)
       return g        

        