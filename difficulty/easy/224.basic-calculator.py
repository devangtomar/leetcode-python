#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#


# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        result = 0  # For the ongoing result
        sign = 1  # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():
                # Building the operand
                operand = (operand * 10) + int(ch)

            elif ch == "+":
                # Add operand to the result with the current sign
                result += sign * operand
                sign = 1
                operand = 0

            elif ch == "-":
                # Add operand to the result with the current sign
                result += sign * operand
                sign = -1
                operand = 0

            elif ch == "(":
                # Push the result and the sign onto the stack, for later
                stack.append(result)
                stack.append(sign)
                # Reset result and sign for the new sub-expression
                sign = 1
                result = 0

            elif ch == ")":
                # Add the last operand to result
                result += sign * operand
                operand = 0
                # Result is multiplied with the sign on top of the stack
                result *= stack.pop()  # stack pop 1, sign
                # Then add to the next element in stack which is the result from previous parentheses
                result += stack.pop()  # stack pop 2, result from before '('

        # Add the last operand in case it was not followed by an operator
        return result + sign * operand


# @lc code=end
