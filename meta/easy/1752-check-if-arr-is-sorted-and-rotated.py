class Solution:
    def check(self, nums: List[int]) -> bool:
        found_peak = nums[-1] > nums[0]

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if not found_peak:
                    found_peak = True
                else:
                    return False

        return True