class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}

        for i, n in enumerate(nums):
            if n in indices and (i - indices[n]) <= k:
                return True
            
            indices[n] = i
        
        return False