"""

Sort input array. Use two pointers just like normal 3sum

Time complexity - O(n^2)
Space complexity - Sorting algorithm dependent - O(n)

"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float("inf")
        nums.sort()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if abs(curr_sum - target) < abs(res - target):
                    res = curr_sum
                
                if curr_sum > target:
                    k -= 1
                else:
                    j += 1
        return res