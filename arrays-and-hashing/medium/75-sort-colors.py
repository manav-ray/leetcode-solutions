class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_counts = [0] * 3
        for n in nums:
            color_counts[n] += 1
        
        pt = 0

        for i, count in enumerate(color_counts):
            while count:
                nums[pt] = i
                pt += 1
                count -= 1