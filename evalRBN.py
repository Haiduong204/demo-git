class Solution(object):
    def evalBPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

    stack = []

    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            # Lấy hai toán hạng từ ngăn xếp
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Chia và làm tròn về 0
                stack.append(int(a / b))
        else:
            # Đẩy số nguyên vào ngăn xếp
            stack.append(int(token))

        # Phần tử cuối cùng là kết quả
        return stack.pop()


S = Solution()
tokens = ["4", "13", "5", "/", "+"]
print(S.evalBPN(tokens))
