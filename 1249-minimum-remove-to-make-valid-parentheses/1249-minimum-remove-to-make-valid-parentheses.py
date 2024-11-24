class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indices = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indices.add(i)
            else:
                stack.pop()

        indices = indices.union(set(stack))
        string = []
        for i, c in enumerate(s):
            if i not in indices:
                string.append(c)

        return "".join(string)