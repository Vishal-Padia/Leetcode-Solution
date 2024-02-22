class Solution:
    def reverse(self, x: int) -> int:
        # Check the sign of x
        sign = 1 if x >= 0 else -1

        # Ensure x is positive for the reversal process
        x *= sign

        rev = 0
        while x > 0:
            a = x % 10
            rev = rev * 10 + a
            x = x // 10

        # Reapply the original sign to the reversed number
        rev *= sign
        # Ensure rev is within the 32-bit signed integer range
        if rev > 2**31 - 1 or rev < -(2**31):
            return 0

        return rev


solution = Solution()

print(solution.reverse(123))  # Output: 321

print(solution.reverse(341))  # Output: 143

print(solution.reverse(-493))  # Output: -394
