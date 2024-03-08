class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0  # Initialize the left pointer to 0
        right = len(s) - 1  # Initialize the right pointer to right of the string
        while left < right:  # run while left is less than right
            while (
                left < right and not s[left].isalnum()
            ):  # Skip non-alphanumeric character by incrementing left pointer
                left += 1  # if it is then increment the left pointer
            while (
                left < right and not s[right].isalnum()
            ):  # Skip non-alphanumeric character by decrementing right pointer
                right -= 1  # if it then decrement the right pointer
            if (
                s[left].lower() != s[right].lower()
            ):  # check if the left character is not same the as right character
                return False  # if they are not same then return false
            else:  # if they are the same then increment left pointer by 1 and decrement the right pointer by 1
                left += 1
                right -= 1

        return True
