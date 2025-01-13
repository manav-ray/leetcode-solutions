class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        dupes = set()

        while r < len(s):
            if s[r] not in dupes:
                dupes.add(s[r])
                r += 1
                res = max(res, (r - l))
            else:
                dupes.remove(s[l])
                l += 1


        return res