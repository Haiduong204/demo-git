class Solution(object):

    # Create function to calculater the largest rectangle area in a histogram

    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0

        # Iterate through each row in the matrix
        for row in matrix:
            for i in range(cols):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            stack = []
            # heights.append(0)
            print(heights)
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)

                stack.append(i)
            print(max_area)
        return max_area


if __name__ == "__main__":
    S = Solution()

    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "1", "1", "1"],
    ]
    print(S.maximalRectangle(matrix))
