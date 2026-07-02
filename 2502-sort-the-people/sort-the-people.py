class Solution(object):
    def sortPeople(self, names, heights):
        d = {}

        for i in range(len(names)):
            d[heights[i]] = names[i]

        heights.sort(reverse=True)

        ans = []

        for h in heights:
            ans.append(d[h])

        return ans