class Solution:
    def isValid(self, s: str) -> bool:
        
        pair = {}
        pair['('] = ')'
        pair['{'] = '}'
        pair['['] = ']'
        
        stack = []
        
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                currPar = stack.pop()
                if pair[currPar] != c:
                    return False
        
        return len(stack) == 0