from typing import List

class Solution:
    """
    There are n kids with candies. You are given an integer array candies, where each candies[i] 
    represents the number of candies the ith kid has, and an integer extraCandies, denoting 
    the number of extra candies that you have.

    Return a boolean array result of length n, where result[i] is true if, after giving the 
    ith kid all the extraCandies, they will have the greatest number of candies among all 
    the kids, or false otherwise.

    Note that multiple kids can have the greatest number of candies.
    
    Approach:
    - Find the maximum number of candies any kid has.
    - For each kid, check if their current candies plus the extra candies would equal or exceed the maximum.
    - Return a boolean array with these results.
    
    Time Complexity: O(n) where n is the number of kids (we iterate through the array once).
    Space Complexity: O(n) for storing the result array.
    """
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = [c + extraCandies >= max_candies for c in candies]
        
        return result

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),   # Example 1
        ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]), # Example 2
        ([12, 1, 12], 10, [True, False, True]),                  # Example 3
        ([1], 1, [True]),                                        # Single kid
        ([5, 5, 5, 5], 0, [True, True, True, True])              # All equal
    ]
    
    for i, (candies, extraCandies, expected) in enumerate(test_cases, 1):
        result = solution.kidsWithCandies(candies, extraCandies)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed: {candies} with {extraCandies} extra -> {result}")
