class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Easiest solution

        # return min(nums)

        # Binary Search
        l, r = 0, len(nums) - 1  # initialize l,r to 0 and len(nums)-1
        while nums[r] < nums[l]:  # whilet the nums[r] element is less than nums[l]
            mid = (l + r) // 2  # get the middle element using  (l+r)//2
            if nums[mid] < nums[r]:  # check if the nums[mid] is less than nums[r]
                r = mid  # if it is then update the r to mid
            else:
                l = mid + 1  # if not then update the l to mid+1 element

        return nums[l]
