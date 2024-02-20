class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) < 2:
        #     return len(s)

        # k, max_len, count = 0, 0, 0

        # # iterating throught the string
        # for i in range(1, len(s)):
        #     for j in range(k, i):
        #         if s[i] == s[j]:
        #             k = j + 1

        #     # Updating the current substring length
        #     count = i - k + 1

        #     # update the maximum length
        #     if count > max_len:
        #         max_len = count

        # return max_len

        # Optimized Approach (Two Pointer Approach)
        charSet = set()  # for keeping the track of characters in the substring
        res = 0  # Store the length of longest substring found

        l = 0  # left pointer of the sliding window
        for r in range(len(s)):  # Iterating over the string with the right pointer
            while (
                s[r] in charSet
            ):  # If the character is found in the set, we shrink the window from left
                charSet.remove(s[l])  # Remove character at the left pointer
                l += 1  # moving the left pointer to the right
            # Adding the current element to the set, as it's not repeated
            charSet.add(s[r])
            res = max(
                res, r - l + 1
            )  # 'r - l + 1' calculates the current substring length
        return res


# Example usage
solution = Solution()

print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3

