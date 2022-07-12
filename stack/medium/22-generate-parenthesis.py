class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        currCombo = []
        
        def generateBacktrack(opened, closed):
            if opened == closed == n:
                res.append(''.join(currCombo))
            
            if opened < n:
                currCombo.append('(')
                generateBacktrack(opened + 1, closed)
                currCombo.pop()
            
            if closed < opened:
                currCombo.append(')')
                generateBacktrack(opened, closed + 1)
                currCombo.pop()
    
        generateBacktrack(0, 0)
        
        return res