class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0

        jewelSet = set(jewels)
        for s in stones:
            if s in jewelSet:
                res += 1

        return res