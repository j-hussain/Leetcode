class Stack:

    def __init__(self) -> None:
        self._data = []

    def __len__(self) -> int:
        # returns length of stack
        return len(self._data)

    def is_empty(self) -> bool:
        # returns True if stack is empty
        return len(self._data) == 0

    def top(self) -> Union[int, str]:
        # return element on top of stack
        if self.is_empty():
            raise Empty("No elements in stack.")
        return self._data[-1]

    def pop(self) -> List:
        if self.is_empty():
            raise Empty("No elements in stack.")
        return self._data.pop()
    
    def push(self, e: str) -> None:
        self._data.append(e)

class Solution:
    def isValid(self, s: str) -> bool:
        opener = "([{"
        closer = ")]}"
        ns = Stack()
        for c in s:
            if c in opener:
                ns.push(c)
            elif c in closer:
                if ns.is_empty():
                    return False
                if closer.index(c) != opener.index(ns.pop()):
                    return
        return ns.is_empty()
            
        