"""

Time complexity - O(n)
Space complexity - O(1)

"""


class Solution:
    def maxScore(self, s: str) -> int:
        res = 0

        ones = 0
        for c in s:
            if c == "1":
                ones += 1
        

        zeros = 0
        for i in range(len(s) -1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
            
            res = max(res, zeros + ones)
        


        return res