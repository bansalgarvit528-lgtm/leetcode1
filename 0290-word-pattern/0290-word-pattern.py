class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if pattern.index(pattern[i]) != words.index(words[i]):
                return False

        return True