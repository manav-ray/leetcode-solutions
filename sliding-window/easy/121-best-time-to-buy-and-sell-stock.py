class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minStock = 100000
        
        for stock in prices:
            minStock = min(stock, minStock)
            res = max(res, stock-minStock)
        
        return res