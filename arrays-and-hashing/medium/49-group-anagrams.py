class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def create_counts(word: str) -> list:
            res = [0] * 26
            for c in word:
                res[ord(c) - ord('a')] += 1
            return str(res)

        word_counts = []
        for s in strs:
            word_counts.append(create_counts(s))
        

        groups = {}

        for i, s in enumerate(strs):
            if word_counts[i] in groups:
                groups[word_counts[i]].append(s)
            else:
                groups[word_counts[i]] = [s]
            
        return list(groups.values())