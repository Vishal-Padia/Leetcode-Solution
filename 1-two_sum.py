class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #    for i in range(len(nums)):
        #        for j in range(i+1, len(nums)):
        #             if nums[i] + nums[j] == target:
        #                 return [i,j]

        # optimized approach
        map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
            map[n] = i
        return []


solution = Solution()

# Example 1
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]

# Example 2
print(solution.twoSum([3, 2, 4], 6))  # Output: [1, 2]

# Example 3
print(solution.twoSum([3, 3], 6))  # Output: [0, 1]