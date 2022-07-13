class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        curr = []
        
        def backtrack(idx):
            
            if sum(curr) == target:
                res.append(curr.copy())
                return
            if idx >= len(candidates) or sum(curr) > target:
                return
            
            curr.append(candidates[idx])
            backtrack(idx)
            curr.pop()
            backtrack(idx+1)
            
        
        backtrack(0)
        
        return res