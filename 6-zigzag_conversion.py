class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (
            numRows == 1
        ):  # If numRows is 1, no zigzag pattern is needed, return original string
            return s

        res = ""  # Initialize an empty string to store the final zigzag pattern result
        for r in range(numRows):  # Iterate over each row of the zigzag pattern
            increment = 2 * (
                numRows - 1
            )  # Calculate the standard increment for the current row
            for i in range(
                r, len(s), increment
            ):  # Iterate through string in steps of 'increment', starting from 'r'
                res += s[i]  # Add character to result
                # Check if middle character exists in zigzag pattern for current row and add it
                if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
                    res += s[
                        i + increment - 2 * r
                    ]  # Add the middle character in the zigzag pattern

        return res  # Return the final zigzag pattern string


solution = Solution()

# Example 1: Convert "PAYPALISHIRING" to a zigzag pattern with 3 rows.
print(solution.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"

# Example 2: Convert "PAYPALISHIRING" to a zigzag pattern with 4 rows.
print(solution.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
