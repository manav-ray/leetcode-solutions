class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        target = len(nums) // 3
        counts = Counter(nums)

        for key, val in counts.items():
            if val > target:
                res.append(key)
            
        
        return res