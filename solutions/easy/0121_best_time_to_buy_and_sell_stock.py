from typing import List

class Solution:
    """
    Given an array 'prices' where prices[i] is the price of a given stock on the ith day, 
    this function returns the maximum profit achievable from a single buy-sell transaction.
    You must buy before you sell, and if no profit is possible, the function returns 0.
    
    Approach:
    - Track the minimum price encountered so far while iterating through the array.
    - For each day, compute the potential profit if selling on that day (current price - min_price).
    - Update the maximum profit if the computed profit is greater than the current max_profit.
    
    Time Complexity: O(n) – Only one pass through the array is required.
    Space Complexity: O(1) – A constant amount of extra space is used.
    """
    
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize min_price to a very high value so any price will be lower.
        min_price = float('inf')
        max_profit = 0
        
        # Iterate through each price in the list.
        for price in prices:
            # If the current price is lower than min_price, update min_price.
            if price < min_price:
                min_price = price
            # Otherwise, check if selling at the current price yields a better profit.
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),  # Best: Buy at 1, sell at 6.
        ([7, 6, 4, 3, 1], 0),     # Prices decrease, so no profit.
        ([1, 2], 1),             # Buy at 1, sell at 2.
        ([3, 2, 6, 5, 0, 3], 4),  # Best: Buy at 2, sell at 6.
    ]
    
    for i, (prices, expected) in enumerate(test_cases, 1):
        result = solution.maxProfit(prices)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed.")
