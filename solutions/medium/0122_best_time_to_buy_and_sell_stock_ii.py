from typing import List

class Solution:
    """
    You are given an integer array 'prices' where prices[i] is the price of a given stock on the ith day.
    
    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
    However, you can buy it then immediately sell it on the same day.
    
    Find and return the maximum profit you can achieve.
    
    Approach:
    - Since you are allowed to complete as many transactions as you like, the idea is to accumulate profit by 
      adding up all positive differences between consecutive days.
    - This means you add (prices[i] - prices[i-1]) to the profit whenever prices[i] > prices[i-1].
    
    Time Complexity: O(n) – We iterate through the list of prices once.
    Space Complexity: O(1) – Only a few extra variables are used.
    """
    
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        # Iterate over prices starting from the second day.
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's, add the difference to the profit.
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
                
        return profit

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # Each test case is a tuple: (prices, expected_profit)
        ([7, 1, 5, 3, 6, 4], 7),   # Buy at 1, sell at 5 => profit=4; buy at 3, sell at 6 => profit=3; total=7.
        ([1, 2, 3, 4, 5], 4),      # Profit = (2-1) + (3-2) + (4-3) + (5-4) = 4.
        ([7, 6, 4, 3, 1], 0),      # Prices are decreasing, so no profit can be made.
        ([1, 2, 1, 2, 1, 2], 3),   # Multiple transactions: (2-1) three times.
    ]
    
    for i, (prices, expected) in enumerate(test_cases, 1):
        result = solution.maxProfit(prices)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed: got {result}.")
