class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        missing = 1

        while missing in num_set:
            missing += 1
        
        return missing