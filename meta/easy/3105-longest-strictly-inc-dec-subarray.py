class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1

        def calcLongest(increasing: bool):
            nonlocal res

            l, r = 0, 1

            while r < len(nums):
                if increasing:
                    while r < len(nums) and nums[r] > nums[r-1]:
                        r += 1
                else:
                    while r < len(nums) and nums[r] < nums[r-1]:
                        r += 1
                
                res = max(res, (r - l))
                l = r
                r += 1
        
        calcLongest(True)
        calcLongest(False)


        return res