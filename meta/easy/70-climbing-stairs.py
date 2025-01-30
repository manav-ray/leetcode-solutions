"""

Like fibonacci sequence

Time complexity - O(n)
Space complexity - O(1)

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        slow = 1
        fast = 2

        for i in range(2, n):
            curr = slow + fast
            slow = fast
            fast = curr

        return fast