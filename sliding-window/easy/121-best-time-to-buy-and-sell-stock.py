class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
                continue
            res = max(res, prices[r] - prices[l])
            r += 1 


        return res
