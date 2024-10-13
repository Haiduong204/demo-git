def largestRectangleArea(heights):
    stack = []
     # Append a zero-height bar at the end to ensure all bars are processed
    max_area = 0
    #add element 0 into array heights 
    heights.append(0)
    n = len(heights)

    #iterate throught all bars 
    for i in range(n):
         # While the stack is not empty and the current bar is shorter than the top of the stack
        while stack and heights[i] < heights[stack[-1]]:
            # Pop the index of the top bar from the stack
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area


heigh = [2, 1, 5]
result = largestRectangleArea(heigh)
print(result)
