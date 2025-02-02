"""

For each char in string, expand outwards while you can create a palindrome
We need to do this for odd and even len SS -> for odd expand one char out left and right
                                              for even expand neighboring char out left and right


Time complexity - O(n^2)
Space complexity - O(1)

"""



class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            l, r = i, i
            res = self.expandPalindromicSubstring(l, r, res, s)
            
        
            l, r = i, i + 1
            res = self.expandPalindromicSubstring(l, r, res, s)
        

        return res
    

    def expandPalindromicSubstring(self, l, r, res, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        curSS = s[l+1:r]
        if len(curSS) > len(res):
            res = curSS
        
        return res