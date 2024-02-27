class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0] # Initialize the maximum subarray with nums[0]
        currSum = 0 # initiaize a currSum = 0 for keeping track of current sum

        for n in nums: # loop through the nums
            if currSum < 0: # check if currSum is less than zero ie negative
                currSum = 0 # if currSum is negative then re-initialize it to 0
            currSum += n # we add the n to the currSum
            maxSub = max(maxSub, currSum) # take the max of maxSub and currSum
        
        return maxSub