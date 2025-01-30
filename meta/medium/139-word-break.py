"""

Bottom-up DP problem:
 - We start at the smallest subproblem -> first char of the big word then build up to the entire word.
 - For a given index i that is anywhere in the string, we say the substring can be formed using word dict words iff:
    1. There is a word in WD that perfectly fits the SS until this index (same size) AND the SS and the word are equal. OR
    2. There is a word in WD that is smaller than the SS, but there is a combination of words from WD that fill up the remaining / beginning of the SS

 - So, we have DP array of s len that represents if the SS until that point is fillable
 - We then go through s idx by idx and increase size with each iteration ->
 - For each of these substrings, we need to perform our core logic described above:
    - Go through each word in wordDict
    - If the length of w > SS len, continue
    - Easy case is if len w == len SS (we can easily check for equality). If equal, we can solve this subproblem so we set the DP at this index to True
    - If this doesn't work, we use cache -> We first check to see if the subproblem until the substring right before the word is added is True
        - If true, we just need to make sure that the remaining word is equal to w. If so, we can solve this subproblem so we set the DP at this index to True
    
Time complexity - O(n * m * k) -> k is avg len of a word in wordDict
Space complexity - O(n)

"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        subproblems = [False] * len(s)


        for i in range(len(s)):
            substring = s[0:i+1]
            for w in wordDict:
                if len(w) > len(substring):
                    continue
                
                if len(w) == len(substring) and w == substring:
                    subproblems[i] = True
                    break

                if subproblems[i - len(w)] and w == s[i - len(w) + 1 : i + 1]:
                    subproblems[i] = True
                    break


        return subproblems[len(s) - 1]