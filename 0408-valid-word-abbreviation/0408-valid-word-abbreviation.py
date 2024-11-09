class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                curr = 0
                while j < len(abbr) and abbr[j].isdigit():
                    if curr == 0 and abbr[j] == "0":
                        return False
                    curr = curr * 10 + int(abbr[j])
                    j += 1
                i += curr
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)