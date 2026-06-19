class Solution:
    def largestAltitude(self, gain):
        alt = [0]

        for x in gain:
            alt.append(alt[-1] + x)

        return max(alt)