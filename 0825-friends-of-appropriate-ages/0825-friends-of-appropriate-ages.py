class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = 0
        hashmap = {}

        for age in ages:
            hashmap[age] = hashmap.get(age, 0) + 1

        for x, nx in hashmap.items():
            for y, ny in hashmap.items():
                if self.valid(x,y):
                    if x == y:
                        count += nx * (nx - 1)
                    else:
                        count += nx * ny
        return count
    def valid(self, x, y):
        return not (y > x or y <= (0.5 * x) + 7)
