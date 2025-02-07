class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        if Counter(s1) != Counter(s2):
            return False
        
        swaps = 0

        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            
            if swaps >= 2:
                return False
            swaps += 1
        

        return True