class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, glob = nums[0], nums[0]
        for i in range(1, len(nums)):
            if curr < 0:
                curr = nums[i]
                
            else:
                curr = curr + nums[i]
                
            if curr > glob:
                glob = curr
                
        return glob