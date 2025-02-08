"""

Bucket sorting - very easy algo and apparently easy to spot as well.

TC - O(n)
SC - O(n)

"""


class Solution:
    def frequencySort(self, s: str) -> str:
        res = ""

        buckets = [[] for _ in range(len(s) + 1)]
        s_count = Counter(s)

        for key, val in s_count.items():
            buckets[val].append(key)


        for i in range(len(buckets) - 1, -1, -1):
            for c in buckets[i]:
                res += i * c 


        return res        
