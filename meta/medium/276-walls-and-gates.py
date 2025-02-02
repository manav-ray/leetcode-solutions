"""

Multi source BFS

Time complexity - O(mn)
Space complexity - O(mn)

"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        visit = set()
        q = deque()

        def addRoom(i, j):
            if (
                i < 0
                or j < 0
                or i >= len(rooms)
                or j >= len(rooms[i])
                or (i, j) in visit
                or rooms[i][j] == -1
            ):
                return

            visit.add((i, j))
            q.append([i, j])

        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    visit.add((i, j))
                    q.append([i, j])

        dist = 0
        while q:
            cur_level_len = len(q)
            for _ in range(cur_level_len):
                i, j = q.popleft()
                rooms[i][j] = dist

                addRoom(i + 1, j)
                addRoom(i - 1, j)
                addRoom(i, j + 1)
                addRoom(i, j - 1)

            dist += 1
