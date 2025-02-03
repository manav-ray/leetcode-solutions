"""

For a 3 letter ss to be palindromic, we need the ends to be the same letter
- So, go through input s and store start and end index of each letter
- After this, for each letter in the map used above, calculate the distinct number
  of letters in between them, then add this number to the result.

Time complexity - O(26n) -> O(n)
Space complexity - O(26) -> O(1)

"""


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        f_and_l_map = defaultdict(lambda: [-1, -1])

        for i, c in enumerate(s):
            if f_and_l_map[c][0] == -1:
                f_and_l_map[c][0] = i
            f_and_l_map[c][1] = i

        res = 0
        
        for i, j in f_and_l_map.values():
            if i == -1 or i == j:
                continue

            dist_alps = set()
            for k in range(i+1, j):
                dist_alps.add(s[k])

            res += len(dist_alps)

        return res