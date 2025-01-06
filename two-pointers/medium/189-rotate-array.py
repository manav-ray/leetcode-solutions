class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = [0] * len(nums)
        for i, n in enumerate(nums):
            tmp[(i + k) % len(nums)] = n
        
        nums[:] = tmp