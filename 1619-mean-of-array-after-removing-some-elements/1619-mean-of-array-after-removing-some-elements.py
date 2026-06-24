class Solution:
    def trimMean(self, arr):
        arr.sort()

        k = len(arr) // 20

        return float(sum(arr[k:-k])) / float(len(arr[k:-k]))