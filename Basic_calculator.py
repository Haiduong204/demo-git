""""
Given a string s representing a valid expression, 
implement a basic calculator to evaluate it,
and return the result of the evaluation.
Input: s = " 2-1 + 2 "
Output: 3
"""

# class Solution:
#     def calculate(self, s: str) -> int:
#         s = s.replace(" ", "")  # Bỏ khoảng trắng
#         stack = []
#         result = 0
#         current_number = 0
#         operation = "+"

#         for i in range(len(s)):
#             char = s[i]
#             if char == "(":
#                 stack.append(result)
#                 stack.append(operation)
#                 result = 0
#                 operation = "+"
#             if char in "+-":
#                 if char == "+":
#                     operation = char
#                 elif char == "-":
#                     operation = char
#             if char.isdigit():
#                 current_number = int(char)
#                 if i == 0 or i == 1:
#                     result = current_number
#                     current_number = 0
#                 else:
#                     if operation == "+":
#                         result += current_number
#                         current_number = 0
#                     elif operation == "-":
#                         result -= current_number
#                         current_number = 0
#             if char == ")":
#                 current_operation = stack.pop()  # Phép toán trước đó
#                 previous_result = stack.pop()  # Kết quả trước đó
#                 if current_operation == "+":
#                     result = previous_result + result
#                 elif current_operation == "-":
#                     result = result - previous_result
#         return result


# class Solution:
#     def calculate(self, s):
#         total = 0
#         i, signs = 0, [1, 1]
#         while i < len(s):
#             c = s[i]
#             if c.isdigit():
#                 start = i
#                 while i < len(s) and s[i].isdigit():
#                     i += 1
#                 total += signs.pop() * int(s[start:i])
#                 continue
#             if c in "+-(":
#                 signs += (signs[-1] * (1, -1)[c == "-"],)
#             elif c == ")":
#                 signs.pop()
#             i += 1
#         return total


# S = Solution()
# s = " 2-1 + 2 "
# print(S.calculate(s))


class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        ans, sign = 0, 1
        n = len(s)
        for i in range(n):
            if s[i].isdigit():
                x = 0
                j = i
                while j < n and s[j].isdigit():
                    x = x * 10 + int(s[j])
                    j += 1
                ans += sign * x
                i = j
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            elif s[i] == "(":
                stk.append(ans)
                stk.append(sign)
                ans, sign = 0, 1
            elif s[i] == ")":
                ans = ans * stk.pop() + stk.pop()
        return ans


S = Solution()
s = "2147483647"
print(S.calculate(s))
