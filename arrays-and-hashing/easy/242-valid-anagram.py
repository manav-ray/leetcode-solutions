class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def create_counts(word: str) -> list:
            res = [0] * 26
            for c in word:
                res[ord(c) - ord('a')] += 1
            return res

        s_count = create_counts(s)
        t_count = create_counts(t)

        return s_count == t_count