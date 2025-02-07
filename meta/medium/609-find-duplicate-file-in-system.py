"""

This is just a string parsing problem. Looking at each elem of the list and make sure you understand the structure.

TC - O(nx) -> x is avg nesting of file in a directory.
SC - O(nx)

"""

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dupes = defaultdict(list)

        for path in paths:
            path_split = path.split(" ")

            for p in path_split:
                start = p.find("(")
                end = p.find(")")

                if start != -1 and end != -1:
                    start += 1
                    content = p[start:end]

                    dupes[content].append(path_split[0] + "/" + p[0:start - 1])
                    
        res = []

        for lists in dupes.values():
            if len(lists) > 1:
                res.append(lists)
        
        return res