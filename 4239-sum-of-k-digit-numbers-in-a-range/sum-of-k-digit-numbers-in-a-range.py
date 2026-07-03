class Solution:
    def sumOfNumbers(self, l,r,k):
        mod = 10**9 + 7

        n = r - l + 1
        s = (l + r) * n // 2

        p1 = pow(n, k - 1, mod)
        p2 = (pow(10, k, mod) - 1) % mod
        inv9 = pow(9, mod - 2, mod)

        return (s * p1 * p2 * inv9) % mod