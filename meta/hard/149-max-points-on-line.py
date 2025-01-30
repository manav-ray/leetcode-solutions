"""

Yes, just because slope is same doesn't mean that two points are on the same line.
HOWEVER, this is in relationship to the origin. In this problem, we calculate the slope in relationship to the point we're checking for.
 - For each point in our list, create a default dict with default 1 (at minimum one point on the line - itself)
 - Use inner loop, calculate slope in relationship to this point. Keep track of counts of each slope.
 - Update res to hold the max count by slope.

Time complexity - O(n^2)
Space complexity - O(n)

"""


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1

        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            slopeCounts = defaultdict(lambda:1)
            for j in range(i + 1, len(points)):
                pX, pY = points[j][0], points[j][1]

                if pX == x:
                    slope = float("inf")
                else:
                    slope = (pY-y) / (pX-x)
                
                slopeCounts[slope] += 1
                res = max(res, slopeCounts[slope])

        return res