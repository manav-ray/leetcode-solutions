class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = sum(nums[:k])
        res = currSum / k
        l, r = 0, k

        while r < len(nums):
            currSum -= nums[l]
            currSum += nums[r]

            res = max(res, currSum / k)

            l += 1
            r += 1


        return res