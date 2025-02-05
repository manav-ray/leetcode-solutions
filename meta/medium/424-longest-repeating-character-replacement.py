"""

Sliding window:
 - Len of a SS is r - l + 1
 - From a SS, if we get the count of max repeating char, remaining chars make rest of SS.
 - So, we add r char and count to map, and while len of SS - max(count) > k, we shorten the SW from left side

TC - O(26n)
SC - O(26) / O(1)

"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        l, r = 0, 0
        counts = defaultdict(int)

        while r < len(s):
            counts[s[r]] += 1
            
            while l <= r and (r - l + 1 - max(counts.values())) > k:
                counts[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

            r += 1



        return res