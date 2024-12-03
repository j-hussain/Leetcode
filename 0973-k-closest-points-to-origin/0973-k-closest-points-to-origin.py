class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0] ** 2 + point[1] ** 2

        heap = [(-distance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(points)):
            dist = -distance(points[i])
            if dist > heap[0][0]:
                heapq.heappushpop(heap, (dist, i))

        return [points[i] for (_, i) in heap]