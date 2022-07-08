class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inverse = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in inverse:
                return [inverse[diff], i]
            else:
                inverse[nums[i]] = i
        
        return [0, 0]