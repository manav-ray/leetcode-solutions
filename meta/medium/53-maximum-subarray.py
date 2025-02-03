"""

Kadane's algorithm -> For some reason you have a pretty strong grasp on this one.

Time complexity - O(n)
Space complexity - O(1)

"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curSum = float("-inf"), 0

        for n in nums:
            curSum += n
            res = max(res, curSum)
            if curSum < 0:
                curSum = 0
                

        return res