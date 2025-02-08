"""

Just need to get number of connected components in the graph - this alg is DFS

TC - O(n^2)
SC - O(n)

"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j] == 1:
                    graph[i].append(j)
        
        res = 0
        visited = set()

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for i in range(len(isConnected)):
            if i in visited:
                continue
            
            dfs(i)
            res += 1

        return res