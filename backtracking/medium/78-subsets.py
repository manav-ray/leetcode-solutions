class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        currSet = []
        
        def backtrack(idx):
            if idx == len(nums):
                res.append(currSet.copy())
                return
            
            currSet.append(nums[idx])
            backtrack(idx+1)
            currSet.pop()
            backtrack(idx+1)
        
        
        backtrack(0)
        
        return res