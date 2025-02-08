"""

TC - O(n * 3^l) -> l = length of word
SC - O(l)

"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(index, i, j, visited):
            if index >= len(word):
                return True

            if (
                i < 0
                or i >= len(board)
                or j < 0
                or j >= len(board[i])
                or board[i][j] != word[index]
                or (i, j) in visited
            ):
                return False

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                visited.add((i, j))
                if dfs(index + 1, i + x, j + y, visited):
                    return True
                visited.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(0, i, j, set()):
                        return True

        return False
