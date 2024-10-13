# class Solution:
#     def maxSlidingWindow(self, nums, k):
#         arr = []
#         n = 0

#         for _ in range(len(nums) - k + 1):
#             print(_)
#             print(nums)
#             for j in range(k):
#                 if nums[j] > n:
#                     n = nums[j]
#             arr.append(n)
#             nums.pop(0)

#         return arr


# S = Solution()
# num = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
# print(S.maxSlidingWindow(num, k))


from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        # Initialize deque to store indices of the elements in nums
        dq = deque()
        # List to store the maximum of each sliding window
        stack = []

        # Loop over each element in the array nums
        for i in range(len(nums)):

            # Remove elements from the deque that are out of the current window
            # The first element in deque corresponds to the oldest index, so check if it is out of the window
            if dq and dq[0] == i - k:
                dq.popleft()  # Remove the oldest element from the deque

            # Maintain deque in decreasing order of elements in nums.
            # Remove elements from the deque from the back that are smaller than the current element nums[i]
            # These elements are no longer useful as nums[i] will be the max in future windows
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()  # Remove smaller elements

            # Add the current index to the deque
            dq.append(i)

            # The largest element in the current window will be at the front of the deque (index dq[0])
            # Start adding to result once we have formed the first window (when i >= k - 1)
            if i >= k - 1:
                stack.append(
                    nums[dq[0]]
                )  # Append the largest element in the current window to result

        # Return the result list containing the maximum of each sliding window
        return stack


S = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(S.maxSlidingWindow(nums, k))
