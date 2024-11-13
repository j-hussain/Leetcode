class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr

        l = 0
        r = len(arr) - k
        while l < r:
            mid = (l+r) // 2
            if x <= arr[mid]:
                r = mid
            elif arr[mid + k] <= x:
                l = mid + 1
            else:
                i = abs(x - arr[mid])
                j = abs(x - arr[mid + k])
                if i <= j:
                    r = mid
                else:
                    l = mid + 1

        return arr[l:l+k]