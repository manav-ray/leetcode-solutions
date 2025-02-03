"""

Prefix sum

Time complexity - O(n) pre O(1) query
Space complexity - O(n)

"""


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []

        curr = 0
        self.prefix_sum.append(curr)
        for n in nums:
            curr += n
            self.prefix_sum.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)