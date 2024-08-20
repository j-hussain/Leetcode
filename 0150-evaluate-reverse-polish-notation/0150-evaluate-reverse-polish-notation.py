class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:
            if token == "+":
                st.append(st.pop() + st.pop())
            elif token == "-":
                second, first = st.pop(), st.pop()
                st.append(first - second)
            elif token == "*":
                st.append(st.pop() * st.pop())
            elif token == "/":
                second, first = st.pop(), st.pop()
                st.append(int(first / second))                
            else:
                st.append(int(token))
        
        return st[0]