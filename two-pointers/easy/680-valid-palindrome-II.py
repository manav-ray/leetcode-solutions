class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindromeHelper(l, r):
            while l <= r:
                if s[l].lower() != s[r].lower():
                    return False
                
                l += 1
                r -= 1
                
            return True
        
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return (palindromeHelper(l+1, r) or palindromeHelper(l, r - 1))
            
            l += 1
            r -= 1
        
        return True