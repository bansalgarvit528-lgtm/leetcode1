class Solution(object):
    def differenceOfSum(self, nums):
        a=sum(nums)
        b=0
        for i in nums:
            while i>0:
                c=i%10
                b=b+c
                i//=10
        return (a-b)        