class SparseVector:
    def __init__(self, nums: List[int]):
        self.values = {i: v for i, v in enumerate(nums) if v}
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum(value * vec.values.get(i, 0) for i, value in self.values.items())

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)