class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        
        if len(digits) == 0:
            return []
        
        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        
        def backtrack(currStr, i):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
        
            chars = mappings[digits[i]]
            
            for c in chars:
                currStr += c
                backtrack(currStr, i+1)
                currStr = currStr[0:-1]
            
        backtrack("", 0)
            
        return res