"""

Very similar to 78. General backtracking algo with dupes
 - Sort input and after popping used element, iterate over input to make sure 
   next addition isn't the same

Time complexity - O(n * 2^n)
Space complexity - O(n)

"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        cur_sub = []
    

        def backtrack(i):
            if i >= len(nums):
                res.append(cur_sub.copy())
                return
            

            cur_sub.append(nums[i])
            backtrack(i + 1)
            cur_sub.pop()
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1)


        backtrack(0)
        return res