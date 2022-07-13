class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        
        
        count = {}
        l, r = 0, 0
        
        while r < len(s):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res,  r-l+1)
            
            r+= 1
        
        
        return res