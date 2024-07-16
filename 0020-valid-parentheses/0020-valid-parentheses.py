class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = "([{"
        closers = ")]}"
        for character in s:
            if character in openers:
                stack.append(character)
            elif character in closers:
                if not stack:
                    return False
                if closers.index(character) != openers.index(stack.pop()):
                    return
        return len(stack) == 0