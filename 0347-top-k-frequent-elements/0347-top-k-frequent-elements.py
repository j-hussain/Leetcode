class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        frequency = c.most_common(k)
        result = []
        for pair in frequency:
            result.append(pair[0])

        return result
        