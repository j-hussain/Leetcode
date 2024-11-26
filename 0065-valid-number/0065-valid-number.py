class Solution:
    def isNumber(self, s: str) -> bool:
        sign, num, dot, exp = False, False, False, False
        for i, c in enumerate(s):
            if c.isdigit():
                num = True
            elif c in ["+", "-"]:
                if i > 0 and s[i-1] not in "eE":
                    return False
            elif c == ".":
                if dot or exp:
                    return False
                dot = True
            elif c in "eE":
                if not num or exp:
                    return False
                exp, num = True, False
            else:
                return False

        return num