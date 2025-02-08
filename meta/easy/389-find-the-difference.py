class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_count = Counter(t)

        for c in s:
            t_count[c] -= 1
        
        for key, val in t_count.items():
            if val > 0:
                return key