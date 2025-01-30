"""

Visualize the matrix and think how you would solve this as a human -> same algorithm 
(change directions if you're at the end or if you are at a cell that you've already visited)

Time complexity - O(n * m)
Space complexity - O(1)

"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        total_elems = len(matrix) * len(matrix[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        fin_track, d_index, i, j = 0, 0, 0, 0

        while fin_track < total_elems:
            res.append(matrix[i][j])
            matrix[i][j] = float("inf")
            direction = directions[d_index]
            if (
                i + direction[0] >= len(matrix)
                or j + direction[1] >= len(matrix[0])
                or matrix[i + direction[0]][j + direction[1]] == float("inf")
            ):
                d_index += 1
                if d_index == 4:
                    d_index = 0

            i += directions[d_index][0]
            j += directions[d_index][1]

            fin_track += 1

        return res
