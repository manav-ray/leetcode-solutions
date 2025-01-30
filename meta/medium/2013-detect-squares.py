"""

Need to find existence of the diagonal point -> x diff == y diff and x, y are different than query point
If such a point exists, find two points that are a combination of query point and found point.
 - i.e query point = (x, y) and found point = (fX, fY) -> Find two points (x, fY) and (fX, y)

Time complexity - O(n)
Space complexity - O(n)

"""


class DetectSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] = self.points.get(tuple(point), 0) + 1

    def count(self, point: List[int]) -> int:
        res = 0
        pX, pY = point[0], point[1]

        for p, count in self.points.items():
            x, y = p[0], p[1]
            if abs(pX - x) == abs(pY - y) and pX != x and pY != y:
                res += count * self.points.get((pX, y), 0) * self.points.get((x, pY), 0)

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)