"""

Very similar to 54 - Spiral Matrix

TC - O(mn)
SC - O(1)

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[float("-inf") for i in range(n)] for j in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d_index, fin_track, i, j = 0, 0, 0, 0

        while fin_track < (m * n):
            if head:
                res[i][j] = head.val
                head = head.next
            else:
                res[i][j] = -1

            fin_track += 1

            curr_dir = directions[d_index]
            if (
                i + curr_dir[0] >= m
                or j + curr_dir[1] >= n
                or res[i + curr_dir[0]][j + curr_dir[1]] != float("-inf")
            ):
                d_index += 1
                if d_index > 3:
                    d_index = 0
            
            i += directions[d_index][0]
            j += directions[d_index][1]

        return res
