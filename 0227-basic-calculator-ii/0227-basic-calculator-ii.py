class Solution:
    def calculate(self, s: str) -> int:
        operators = set(["+", "-", "/", "*"])
        number = 0
        stack = []
        current_op = "+"
        for i, c in enumerate(s):
            if c.isdigit():
                number = number * 10 + int(c)
            if c in operators or i == len(s) - 1:
                if current_op == "+":
                    stack.append(number)
                elif current_op == "-":
                    stack.append(-number)
                elif current_op == "*":
                    stack.append(stack.pop() * number)
                elif current_op == "/":
                    stack.append(int(stack.pop() / number))
                current_op = c
                number = 0

        return sum(stack)
