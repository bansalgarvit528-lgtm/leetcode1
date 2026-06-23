class Solution:
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort()

            y = stones.pop()   # largest stone
            x = stones.pop()   # second largest stone

            if x != y:
                stones.append(y - x)

        if stones:
            return stones[0]
        return 0