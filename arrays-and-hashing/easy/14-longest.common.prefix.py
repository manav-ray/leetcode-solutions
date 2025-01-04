class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i, c in enumerate(strs[0]):
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return res

            res += c

        return res