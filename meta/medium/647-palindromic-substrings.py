"""

Very similar to #5 - longest palindromic substring.

TC - O(n)
SC - O(1)

"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            l, r = i, i
            res += self.getAllPalindromesCount(l, r, s)

            l, r = i, i + 1
            res += self.getAllPalindromesCount(l, r, s)


        return res


    def getAllPalindromesCount(self, l, r, s):
        count = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

        return count