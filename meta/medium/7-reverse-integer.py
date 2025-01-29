"""

x % 10 gives ones digit of x
x // 10 removes ones digit of x

Time complexity - O(log x) -> Roughly log(x) digits in x
Space complexity - O(1)

"""


class Solution:
    def reverse(self, x: int) -> int:
        MAX = (2 ** 31) - 1

        sign = 1
        if x < 0:
            sign = -1

        x = abs(x)

        res = 0

        while x:
            res = (res * 10) + (x % 10)
            x = x // 10

            if res > MAX:
                return 0

        return res * sign