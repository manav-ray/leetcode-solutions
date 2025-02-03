"""

You know that XOR two numbers results in 0. This is the logic behind this problem.
For a list that's supposed to contain 0..n, it's len would be n and each element in the list
would essentially be an index of that list, although not in order.

 - So, we have a way to guarantee two same numbers check -> index and element
 - Iterate from 0..n, XOR both index and element. Every index is available but not every element,
   XORing the index but not the missing element results in bit manipulation automatically giving us
   the repsonse.

Time complexity - O(n)
Space complexity - O(1)

"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0

        for i in range(len(nums) + 1):
            if i < len(nums):
                missing ^= i ^ nums[i]
            else:
                missing ^= i

        return missing