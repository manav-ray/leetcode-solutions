"""

Edge cases - read problem carefully and ask edge case questions

Time complexity - O(n)
Space complexity - O(1)

"""


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0
        
        ptr = 0
        sign = 1
        if s[ptr] == "-":
            sign = -1
            ptr += 1
        elif s[ptr] == "+":
            ptr += 1
        

        res = 0

        while ptr < len(s):
            if not s[ptr].isdigit():
                break
            
            res = (res * 10) + int(s[ptr])
            ptr += 1

        res = res * sign
        if res > (2 ** 31) - 1:
            return (2 ** 31) - 1
        elif res < (-2 ** 31):
            return (-2 ** 31)

        return res