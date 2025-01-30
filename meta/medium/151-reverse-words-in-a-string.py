"""

Time complexity - O(n)
Space complexity - O(n)

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        splitS = s.split()

        res = ""

        for i in range(len(splitS) - 1, -1, -1):
            res += splitS[i]
            if i != 0:
                res += " "
        
        return res