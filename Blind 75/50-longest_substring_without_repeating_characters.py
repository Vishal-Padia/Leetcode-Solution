class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()  # Initialize a set for keeping track of characters in substring
        res = 0  # store the length of longest substring found

        l = 0  # left pointer for sliding window
        for r in range(len(s)):  # Run a for loop through the length of string
            while (
                s[r] in charSet
            ):  # while the s[r] character is in the set, shrink the window from left
                charSet.remove(s[l])  # remove the character at the left pointer
                l += 1  # moving the left pointer to the right
            charSet.add(
                s[r]
            )  # adding the current element to the set, as it's not repeated
            res = max(
                res, r - l + 1
            )  # update the result with the max of result and  'r-l+1'
        return res
