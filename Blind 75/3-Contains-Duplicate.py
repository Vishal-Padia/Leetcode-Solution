class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_set = set(nums)  # Initialize a set of nums
        if len(new_set) == len(
            nums
        ):  # Check whether the len(set) is equal to the len(nums)
            return False  # If it is equal then return False becuase a set cannot contain duplicate values
        else:
            return True  # if it contains duplicate values the length won't be the same therefore we return True
