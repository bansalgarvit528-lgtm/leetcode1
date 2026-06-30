class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count = 0

        for word in words:
            ok = True

            for ch in word:
                if ch not in allowed:
                    ok = False
                    break

            if ok:
                count += 1

        return count