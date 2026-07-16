class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def gcdSum(self, nums):
        prefix = []
        mx = 0

        # Create prefixGcd array
        for x in nums:
            if x > mx:
                mx = x
            prefix.append(self.gcd(x, mx))

        # Sort the array
        prefix.sort()

        ans = 0
        i = 0
        j = len(prefix) - 1

        # Pair smallest with largest
        while i < j:
            ans += self.gcd(prefix[i], prefix[j])
            i += 1
            j -= 1

        return ans