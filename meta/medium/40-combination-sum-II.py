"""

Similar to #39 -> only difference is candidates contains duplicates and cannot reuse same element.

Time complexity - O(n * 2^n)
Space complexity - O(target * n)

"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr_combo = []
        candidates.sort()


        def backtrack(i, total):
            if total == target:
                res.append(curr_combo.copy())
                return
            
            if i >= len(candidates) or total > target:
                return

            curr_combo.append(candidates[i])
            backtrack(i + 1, total + candidates[i])
            curr_combo.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
                
            backtrack(i + 1, total)
        

        backtrack(0, 0)
        return res