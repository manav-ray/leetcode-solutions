class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1

        if len(needle) > len(haystack):
            return -1

        windowLen = len(needle)

        for i in range(len(haystack) - windowLen + 1):
            if haystack[i:i+windowLen] == needle:
                return i


        return res