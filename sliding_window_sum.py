from collections import deque


class Solution:
    def SumSlidingWindow(self, nums, k):
        # arr = []
        # sum = 0
        # max_sum = 0

        # for i in range(len(nums) - k + 1):
        #     for j in range(i, i + k):
        #         sum = sum + nums[j]

        #     arr.append(sum)
        #     max_sum = max(max_sum, sum)
        #     sum = 0
        # return max_sum
        if len(nums) < k:
            print("invalid")

        window_sum = sum(arr[:k])

        max_sum = window_sum

        for i in range(len(nums) - k):
            window_sum = window_sum - nums[i] + nums[i + k]
            max_sum = max(max_sum, window_sum)
        return max_sum


if __name__ == "__main__":
    S = Solution()
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    print(S.SumSlidingWindow(arr, k))
