class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]  # Set the initial buying prices as the first element of array
        max_profit = (
            0  # declare a max_profit variable where we will store the maximum profit
        )
        for i in range(1, len(prices)):
            if buy > prices[i]:
                buy = prices[
                    i
                ]  # Update the buying price if the buying price is greater than the price at index i
            elif prices[i] - buy > max_profit:
                max_profit = (
                    prices[i] - buy
                )  # update the max_profit if the price at i - buy is greater than the max_profit
        return max_profit
