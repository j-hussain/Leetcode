from math import ceil, log
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets < 2:
            return 0
        k = minutesToTest / minutesToDie
        return ceil( log(buckets) / log(k+1) )