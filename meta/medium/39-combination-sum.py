"""

General backtracking algo

Time complexity - O(n * 2^n) -> n because sum.copy(), 2^n since we have two decisions per element of the array (to include or not to include)
Space complexity - O(target * n) -> O(n) since we're storing sum array and target since that is the maximum recursive call stack depth

"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr_sum = []

        def backtrack(i, total):
            if total == target:
                res.append(curr_sum.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            

            curr_sum.append(candidates[i])
            backtrack(i, total + candidates[i])
            curr_sum.pop()
            backtrack(i+1, total)
        
        backtrack(0, 0)

        return res