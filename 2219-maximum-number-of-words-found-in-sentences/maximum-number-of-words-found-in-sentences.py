class Solution:
    def mostWordsFound(self, sentences):
        ans = 0

        for sentence in sentences:
            words = sentence.split()
            ans = max(ans, len(words))

        return ans