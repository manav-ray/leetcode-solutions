class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        counts = Counter(nums)
        heap = [(-count, num) for num, count in counts.items()]

        heapq.heapify(heap)

        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1

        return res