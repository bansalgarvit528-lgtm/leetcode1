class Solution(object):
    def runningSum(self, nums):
      count=0
      a=[]
      for i in nums:
        count+=i
        a.append(count)
      return a
        