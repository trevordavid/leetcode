from typing import List

class Solution:
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the 
    product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.

    Example:
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        Explanation:
            - answer[0] = 2*3*4 = 24
            - answer[1] = 1*3*4 = 12
            - answer[2] = 1*2*4 = 8
            - answer[3] = 1*2*3 = 6

    Example:
        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,-9,0,0]
        Explanation: Since there's a 0 in the input, most elements in output become 0.
    """
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculate product of all elements except self without division.
        
        Approach:
        - Using two passes through the array (left-to-right and right-to-left)
        - First pass: compute product of all elements to the left of each index
        - Second pass: compute product of all elements to the right and multiply with left products
        
        Time Complexity: O(n) where n is the length of the array
                       - We do two passes through the array, each taking O(n)
        
        Space Complexity: O(1) excluding the output array
                       - We only use a constant amount of extra space
        
        Args:
            nums: List of integers
            
        Returns:
            List of products where each element is the product of all numbers except the current one
        """
        n = len(nums)
        result = [1] * n  # Initialize result array with 1's
        
        # First pass: Calculate products of all elements to the left
        left_product = 1
        for i in range(n):
            result[i] = left_product  # Store product of all elements to the left
            left_product *= nums[i]  # Update running product
        
        # Second pass: Calculate products of all elements to the right and multiply with left products
        right_product = 1
        # Iterate from right to left
        for i in range(n-1, -1, -1):
            result[i] *= right_product  # Multiply by product of all elements to the right
            right_product *= nums[i]  # Update running product
        
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),                # Example 1
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),          # Example 2 with 0
        ([2, 3, 4, 5], [60, 40, 30, 24]),              # All positive
        ([-2, -3, 4, -5], [60, 40, -30, 24]),          # Mix of positive/negative
        ([0, 0], [0, 0]),                              # Multiple zeros
        ([1], [1]),                                     # Single element
        ([1, 1, 1, 1], [1, 1, 1, 1]),                  # All same value
    ]
    
    print("Testing without division (required approach):")
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.productExceptSelf(nums)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Got {result}, Expected {expected}")
    
