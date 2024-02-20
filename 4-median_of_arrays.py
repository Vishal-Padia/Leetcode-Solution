import numpy as np


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Using numpy
        # df = np.concatenate((nums1, nums2), axis=0)
        # return np.median(df)

        # Without using numpy
        combined_arr = nums1 + nums2
        combined_arr.sort()
        n = len(combined_arr)
        if n % 2 == 0:
            med1 = combined_arr[n // 2]
            med2 = combined_arr[n // 2 - 1]
            median = (med1 + med2) / 2
            return median
        else:
            return combined_arr[n // 2]


# Example usage
solution = Solution()

print(solution.findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
print(solution.findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5
print(solution.findMedianSortedArrays([], [1]))  # Output: 1.0
