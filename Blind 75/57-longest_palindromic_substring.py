class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""  # Initialize the result string to store the longest palindrome found.
        resLen = 0  # Initialize the length of the longest palindrome found to 0.

        for i in range(len(s)):  # Iterate through each character in the string.
            # Check for odd-length palindrome with center at i.
            l, r = i, i  # Set left and right pointers at the current character.
            while (
                l >= 0 and r < len(s) and s[l] == s[r]
            ):  # Expand while characters match and within bounds.
                if (
                    r - l + 1
                ) > resLen:  # Update result if a longer palindrome is found.
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1  # Move left pointer leftward.
                r += 1  # Move right pointer rightward.

            # Check for even-length palindrome with center between i and i+1.
            l, r = i, i + 1  # Set left pointer at i and right pointer at i+1.
            while (
                l >= 0 and r < len(s) and s[l] == s[r]
            ):  # Expand while characters match and within bounds.
                if (
                    r - l + 1
                ) > resLen:  # Update result if a longer palindrome is found.
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1  # Move left pointer leftward.
                r += 1  # Move right pointer rightward.

        return res  # Return the longest palindrome found.
