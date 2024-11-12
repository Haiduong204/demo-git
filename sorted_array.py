# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         # Merge the arrays into a single sorted array.
#         merged = nums1 + nums2

#         # Sort the merged array.
#         merged.sort()

#         # Calculate the total number of elements in the merged array.
#         total = len(merged)

#         if total % 2 == 1:
#             # If the total number of elements is odd, return the middle element as the median.
#             return float(merged[total // 2])
#         else:
#             # If the total number of elements is even, calculate the average of the two middle elements as the median.
#             middle1 = merged[total // 2 - 1]
#             middle2 = merged[total // 2]
#             return (float(middle1) + float(middle2)) / 2.0


# S = Solution()
# nums1 = [1, 2]
# nums2 = [3, 4]
# print(S.findMedianSortedArrays(nums1, nums2))


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            findMedianSortedArrays(nums2, nums1)

        left = (n1 + n2 + 1) // 2
        n = n1 + n2
        low = 0
        high = n1

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1

            l1 = float("-inf")
            l2 = float("-inf")
            r1 = float("inf")
            r2 = float("inf")

            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]

            if r1 >= l2 and r2 >= l1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            if r1 < l2:
                low = mid1 + 1
            if r2 < l1:
                high = mid1 - 1

        return 0


S = Solution()
nums1 = [1, 2]
nums2 = [3, 4]
print(S.findMedianSortedArrays(nums1, nums2))
