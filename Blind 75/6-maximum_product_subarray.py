class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)  # size of array.

        pre, suff = 1, 1  # initialize the prefix and suffix to 1
        ans = float("-inf")  # initialize ans to float('-inf')
        for i in range(n):  # loop through the size of list
            if pre == 0:  # check if pre is 0
                pre = 1  # if pre is 0 we start again, pre = 1
            if suff == 0:  # check if suff is 0
                suff = 1  # if suff is 0 we start again, suff = 1
            pre = pre * nums[i]  # update pre with the product of pre and nums[i]
            suff = (
                suff * nums[n - i - 1]
            )  # update suff with the product of suff and nums[n - i - 1]
            ans = max(
                ans, max(pre, suff)
            )  # update the ans with max of ans and max of pre,suff
        return ans  # return ans

        # Kandane's algorithm
        # prod1 = nums[0]
        # prod2 = nums[0]
        # result = nums[0]

        # for i in range(1, len(nums)):
        #     temp = max(nums[i], prod1 * nums[i], prod2 * nums[i])
        #     prod2 = min(nums[i], prod1 * nums[i], prod2 * nums[i])
        #     prod1 = temp

        #     result = max(result, prod1)

        # return result
