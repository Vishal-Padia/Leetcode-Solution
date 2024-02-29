class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0  # Initialize the low as 0
        high = len(nums) - 1  # Initialize the high as length - 1
        while low <= high:  # continue as long a low is less than or equal to high
            mid = (low + high) // 2  # calculate mid using average of low and high

            if nums[mid] == target:  # check if the middle element is the target
                return mid  # return the mid if it's the mid

            if (
                nums[mid] >= nums[low]
            ):  # check if the mid is greater than or equal to the low
                if (
                    target > nums[mid] or target < nums[low]
                ):  # if it is then check target is greater than mid or target is less than low
                    low = mid + 1  # if it is then update low to mid + 1
                else:
                    high = mid - 1  # if not then update high to mid - 1
            else:
                if (
                    target < nums[mid] or target > nums[low]
                ):  # check if the target is less than mid or target is greater than low
                    high = mid - 1  # if it is then update high to mid - 1
                else:
                    low = mid + 1  # if not then update low to mid + 1

        return -1  # if not found then return -1
