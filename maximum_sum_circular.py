"""
Given a circular integer array nums of length n, 
return the maximum possible sum of a non-empty subarray of nums.
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
"""


def maxSubarraySumCircular(A):
    total, maxSum, curMax, minSum, curMin = 0, A[0], 0, A[0], 0
    for a in A:
        curMax = max(curMax + a, a)
        maxSum = max(maxSum, curMax)
        curMin = min(curMin + a, a)
        minSum = min(minSum, curMin)
        total += a
    return max(maxSum, total - minSum) if maxSum > 0 else maxSum


nums = [1, -2, 3, -2]
print(maxSubarraySumCircular(nums))
