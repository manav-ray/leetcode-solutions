"""

Binary search - lower bound = largest weight, upper bound = sum of all weights

Time complexity - O(nlog(n))
Space complexity - O(1)

"""


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            dayCount = 1
            currLoad = 0

            for w in weights:
                currLoad += w
                if currLoad > cap:
                    dayCount += 1
                    currLoad = w
            
            return dayCount <= days


        while l <= r:
            m = (l + r) // 2

            if canShip(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
            
        return res