class Solution:

    def __init__(self, w: List[int]):
        self.sums = []
        pre_sum = 0
        for weight in w:
            pre_sum += weight
            self.sums.append(pre_sum)
        self.total = pre_sum

    def pickIndex(self) -> int:
        target = self.total * random.random()
        l, r = 0, len(self.sums)
        while l < r:
            mid = (l + r) // 2
            if target > self.sums[mid]:
                l = mid + 1
            else:
                r = mid

        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()