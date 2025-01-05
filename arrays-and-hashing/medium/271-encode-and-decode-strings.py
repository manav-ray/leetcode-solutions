class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s 

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            
            s_len = int(s[i:j])
            res.append(s[j+1:j+s_len+1])

            i = s_len + j + 1


        return res