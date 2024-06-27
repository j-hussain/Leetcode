class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #mapping char count to list of anagrams
        for s in strs:
            count = [0] * 26 # 26 possible characters [a-z]

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return result.values()