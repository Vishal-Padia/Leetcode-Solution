class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix and Suffix Product
        n = len(nums)
        prefixProduct = [
            0
        ] * n  # initialize a prefixProduct list consisting of 0 of size n
        suffixProduct = [
            0
        ] * n  # initialize a suffixProduct list consisting of 0 of size n
        product = [0] * n  # initialize a product list consisting of 0 of size n

        prefixProduct[0] = 1  # update the first element of prefixProduct to 1
        for i in range(1, n):  # loop starting from 1 to n
            prefixProduct[i] = (
                nums[i - 1] * prefixProduct[i - 1]
            )  # update the prefixProduct to multiplication of nums[i-1] and prefixProduct[i-1]

        suffixProduct[n - 1] = 1  # update the n-1 position of suffixProduct to 1
        for i in range(
            n - 2, -1, -1
        ):  # loop starting from n-2 and stoping at -1 with a increment of -1
            suffixProduct[i] = (
                nums[i + 1] * suffixProduct[i + 1]
            )  # update the suffixProduct to multiplication of nums[i+1] and suffixProduct[i+1]

        for i in range(n):  # loop through n
            product[i] = (
                prefixProduct[i] * suffixProduct[i]
            )  # update the product with multiplication of prefixProduct and suffixProduct

        return product
