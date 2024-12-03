class Solution:
    def customSortString(self, order: str, s: str) -> str:
        from collections import Counter
        count = Counter(s)
        res = []
        for char in order:
            if char in count:
                res.append(char * count[char])
                del count[char]
        for char, freq in count.items():
            res.append(char * freq)

        return "".join(res)