class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
       count=nums1+nums2
       count.sort()
       n=len(count)
       if n % 2!=0:
        return count[n//2]
       else:
        return (count[n//2] + count[n//2-1])/2.0
        
        