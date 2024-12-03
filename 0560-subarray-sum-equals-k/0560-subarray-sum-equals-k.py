class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = {0: 1}
        count = 0
        cumulative_sum = 0
        for num in nums:
            cumulative_sum += num
            difference = cumulative_sum - k
            if difference in cache:
                count += cache[difference]
            cache[cumulative_sum] = cache.get(cumulative_sum, 0) + 1

        return count