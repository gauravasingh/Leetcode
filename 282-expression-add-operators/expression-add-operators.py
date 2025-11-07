from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def backtrack(index: int, expr: str, value: int, last: int):
            # If we reached the end of the string
            if index == len(num):
                # If expression evaluates to target, add to results
                if value == target:
                    res.append(expr)
                return

            for i in range(index, len(num)):
                # Avoid numbers with leading zeros
                if i != index and num[index] == '0':
                    break

                curr_str = num[index:i + 1]
                curr_num = int(curr_str)

                if index == 0:
                    # First number, start the expression
                    backtrack(i + 1, curr_str, curr_num, curr_num)
                else:
                    # Addition
                    backtrack(i + 1, expr + '+' + curr_str, value + curr_num, curr_num)
                    # Subtraction
                    backtrack(i + 1, expr + '-' + curr_str, value - curr_num, -curr_num)
                    # Multiplication
                    backtrack(i + 1, expr + '*' + curr_str,
                              value - last + last * curr_num, last * curr_num)

        backtrack(0, "", 0, 0)
        return res
