from typing import List

class Solution:
    """
    Given an integer array nums, find a contiguous subarray that has the largest product, 
    and return the product. The test cases are generated so that the answer will fit in 
    a 32-bit integer.
    
    Approach:
    - Use dynamic programming with two variables: `cur_max` (maximum product ending at current index) 
      and `cur_min` (minimum product ending at current index).
    - Since negative numbers can flip the sign, `cur_min` helps track the smallest product,
      which could become the largest if multiplied by a negative number.
    - The result is updated at each step with the maximum product found so far.

    Time Complexity: O(N) – We iterate through the array once.
    Space Complexity: O(1) – Only a few extra variables are used.
    """

    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Edge case: empty list

        res = max(nums)  # Initialize result with the maximum single element
        cur_max, cur_min = 1, 1  # Tracks max and min products

        for n in nums:
            temp_max = cur_max * n  # Store cur_max before updating cur_min
            cur_max = max(temp_max, cur_min * n, n)
            cur_min = min(temp_max, cur_min * n, n)
            res = max(res, cur_max)
        
        return res


# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 3, -2, 4], 6),        # Subarray: [2, 3]
        ([-2, 0, -1], 0),          # Single zero is max
        ([1, 2, 3, 4], 24),        # Entire array is max product
        ([-1, -2, -3, -4], 24),    # Even count of negatives => multiply to positive
        ([0, -2, -3, -4, 0], 12),  # Subarray [-3, -4] has max product
        ([3, -1, 4], 4),           # Single element case
        ([-3, -1, -1], 3),         # Single-element max (odd negatives)
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = solution.maxProduct(nums)
        assert result == expected, f"Test {i + 1} failed: Expected {expected}, got {result}"
        print(f"Test {i + 1} passed.")
