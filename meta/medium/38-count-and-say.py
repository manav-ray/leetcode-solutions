"""

Easy problem - pay close attention to what it's actually asking

"""

class Solution:
    def countAndSay(self, n: int) -> str:

        def countAndSayHelper(s):
            seq = ""
            l, r = 0, 0

            while r < len(s):
                while r < len(s) and s[l] == s[r]:
                    r += 1
                
                seq += str(r-l) + s[l]
                l = r
            
            return seq
        
        res = "1"
        for i in range(2, n + 1):
            res = countAndSayHelper(res)
        

        return res