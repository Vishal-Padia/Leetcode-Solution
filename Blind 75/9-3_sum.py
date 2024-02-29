class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()  # Initialize a set
        nums.sort()  # sort the list
        n = len(nums)  # initialize n as the length of nums
        for i in range(n - 2):  # run a loop for n - 2
            j = i + 1  # initialize j as i + 1
            k = n - 1  # initialize k as n - 1
            while j < k:  # continue while j is less than k
                temp = (
                    nums[i] + nums[j] + nums[k]
                )  # initialize temp as addition nums of i, j, k
                if temp == 0:  # check if the temp is 0
                    ans.add(
                        (nums[i], nums[j], nums[k])
                    )  # If the temp is 0, add nums of i, j, k to the ans
                    j += 1  # increment j by 1
                elif temp > 0:  # check if the temp is greater than 0
                    k -= 1  # if it is decrement k by 1
                else:
                    j += 1  # otherwise increment j by 1
        return ans
