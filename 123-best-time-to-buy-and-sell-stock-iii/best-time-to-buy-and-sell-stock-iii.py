class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # Initialize profits
        first_buy = float('-inf')
        first_sell = 0
        second_buy = float('-inf')
        second_sell = 0

        for price in prices:
            # Update states in order
            first_buy = max(first_buy, -price)             # Best profit after first buy
            first_sell = max(first_sell, first_buy + price) # Best profit after first sell
            second_buy = max(second_buy, first_sell - price) # Best profit after second buy
            second_sell = max(second_sell, second_buy + price) # Best profit after second sell

        return second_sell
