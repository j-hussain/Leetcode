class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        string = ""
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((string, num))
                string = ""
                num = 0
            elif char == ']':
                last, x = stack.pop()
                string = last + string * x
            else:
                string += char
        
        return string
