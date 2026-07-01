class Solution(object):
    def numSpecialEquivGroups(self, words):
        groups = set()

        for word in words:
            even = ""
            odd = ""

            for i in range(len(word)):
                if i % 2 == 0:
                    even += word[i]
                else:
                    odd += word[i]

            even = "".join(sorted(even))
            odd = "".join(sorted(odd))

            groups.add(even + "#" + odd)

        return len(groups)