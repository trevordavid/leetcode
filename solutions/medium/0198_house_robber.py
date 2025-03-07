from typing import List

class Solution:
    """
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
    but adjacent houses have security systems connected, so if two adjacent houses are robbed on the same night, the police
    will be alerted.
    
    Given an integer array 'nums' representing the amount of money at each house, return the maximum amount of money you
    can rob tonight without alerting the police.
    
    Approach:
    - For each house, you have two choices:
      1. Skip the current house, so the maximum profit remains the same as for the previous house (profit[i-1]).
      2. Rob the current house and add its value to the maximum profit from two houses back (nums[i] + profit[i-2]).
    - This gives the recurrence relation:
        profit[i] = max(profit[i-1], nums[i] + profit[i-2])
    - Handle edge cases:
      - If there's only one house, return its value.
      - If there are two houses, return the maximum of the two.
    
    Time Complexity: O(n) – iterating through the houses once.
    Space Complexity: O(n) – for the profit list.
    """
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Base case: if there is only one house, return its value.
        if n == 1:
            return nums[0]
        
        # Initialize the profit list
        profit = [0] * n
        profit[0] = nums[0]                # Profit for the first house.
        profit[1] = max(nums[0], nums[1])   # For the first two houses, choose the maximum.
        
        # Compute the maximum profit for each house starting from index 2.
        for i in range(2, n):
            profit[i] = max(profit[i-1], nums[i] + profit[i-2])
        
        # The last element holds the maximum profit achievable.
        return profit[-1]

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([1, 2, 3, 1], 4),          # Rob houses 1 and 3: 1 + 3 = 4.
        ([2, 7, 9, 3, 1], 12),       # Rob houses 1, 3, and 5: 2 + 9 + 1 = 12.
        ([2, 1, 1, 2], 4),          # Rob houses 1 and 4: 2 + 2 = 4.
        ([0], 0),                   # Single house with no money.
        ([1, 2], 2),                # Choose the maximum of the two houses.
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.rob(nums)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed.")
