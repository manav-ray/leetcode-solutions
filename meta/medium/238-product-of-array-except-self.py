class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        pre = 1
        for i in range(len(nums)):
            prefix[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = post
            post *= nums[i]

        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

        return res