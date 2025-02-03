"""

Generic backtrack aglo

Time complexity - O(n * 2^n)
Space complexity - O(n)

"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur_sub = []
    

        def backtrack(i):
            if i >= len(nums):
                res.append(cur_sub.copy())
                return
            

            cur_sub.append(nums[i])
            backtrack(i + 1)
            cur_sub.pop()
            backtrack(i + 1)


        backtrack(0)
        return res