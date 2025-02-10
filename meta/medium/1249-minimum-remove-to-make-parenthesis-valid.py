class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        filtered = ""
        diff = 0

        for c in s:
            if c == "(":
                diff += 1
                filtered += c
            elif c == ")" and diff > 0:
                diff -= 1
                filtered += c
            elif c != ")" and c != "(":
                filtered += c
        
        res = ""
        for c in filtered[::-1]:
            
            if c == "(" and diff > 0:
                diff -= 1
            else:
                res += c
        
        return res[::-1]