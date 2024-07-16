class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if operation == "C":
                if len(record) != 0:
                    record.pop()
            elif operation == "D":
                if len(record) != 0:
                    x = int(record[-1]) * 2
                    record.append(x)
            elif operation == "+":
                if len(record) >= 2:
                    x = record[-1] + record[-2]
                    record.append(x)
            else:
                record.append(int(operation))
        return sum(record)