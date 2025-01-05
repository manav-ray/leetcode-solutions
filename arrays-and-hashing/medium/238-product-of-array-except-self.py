class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)


        pre = []
        mul = 1
        for n in nums:
            mul *= n
            pre.append(mul)

        post = [0] * len(nums)
        mul = 1
        for i in range(len(nums) -1, -1, -1):
            mul *= nums[i]
            post[i] = mul

        res[0] = post[1]
        res[len(res) - 1] = pre[len(pre) - 2]

        for i in range(1, len(nums) - 1):
            res[i] = pre[i-1] * post[i+1]


        return res