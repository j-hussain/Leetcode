class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        counter = Counter(nums)
        heap = [(-value, i) for i, value in counter.items()]
        heapq.heapify(heap)
        result = []
        for i in range(k):
            e = heapq.heappop(heap)
            result.append(e[1])

        return result