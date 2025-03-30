from typing import List

# Given an integer array nums, find the subarray with the largest sum, and return its sum.


class Solution:
    """
    Given an integer array nums, find the subarray with the largest sum, and return its sum.
    
    A subarray is a contiguous subset of the array.
    
    Example:
        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: The subarray [4,-1,2,1] has the largest sum 6.
        
    Example:
        Input: nums = [1]
        Output: 1
        Explanation: The subarray [1] has the largest sum 1.
        
    Example:
        Input: nums = [5,4,-1,7,8]
        Output: 23
        Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
    """
    
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find the maximum subarray sum using Kadane's algorithm.
        
        Approach:
        - Iterate through the array, keeping track of the current sum and maximum sum seen so far
        - For each element, decide whether to start a new subarray or extend the current one
        - Update the maximum sum if the current sum is larger
        
        Time Complexity: O(n) where n is the length of the array
                       - We only need to iterate through the array once
        
        Space Complexity: O(1) - we only use two variables regardless of input size
        
        Args:
            nums: List of integers
            
        Returns:
            Maximum sum of any contiguous subarray
        """
        
        maxSum = nums[0]
        currentSum = nums[0]

        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum
    
    def maxSubArrayDivideConquer(self, nums: List[int]) -> int:
        """
        Find the maximum subarray sum using divide and conquer approach.
        
        Approach:
        - Divide the array into halves until we reach base case (1 element)
        - Find the maximum subarray sum in the left half, right half, and crossing the middle
        - Return the maximum of these three values
        
        Time Complexity: O(n log n) where n is the length of the array
                       - We recursively divide the array in half
                       - At each level, we do O(n) work to find the crossing sum
        
        Space Complexity: O(log n) due to the recursion stack
        
        Args:
            nums: List of integers
            
        Returns:
            Maximum sum of any contiguous subarray
        """
        def find_max_crossing_sum(nums, low, mid, high):
            # Find the maximum sum starting from mid and going left
            left_sum = float('-inf')
            current_sum = 0
            for i in range(mid, low - 1, -1):
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)
            
            # Find the maximum sum starting from mid+1 and going right
            right_sum = float('-inf')
            current_sum = 0
            for i in range(mid + 1, high + 1):
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)
            
            # Return the sum of the two halves
            return left_sum + right_sum
        
        def find_max_subarray(nums, low, high):
            # Base case: only one element
            if low == high:
                return nums[low]
            
            # Divide the array into two halves
            mid = (low + high) // 2
            
            # Find the maximum sum in left and right halves
            left_max = find_max_subarray(nums, low, mid)
            right_max = find_max_subarray(nums, mid + 1, high)
            
            # Find the maximum sum crossing the middle
            crossing_max = find_max_crossing_sum(nums, low, mid, high)
            
            # Return the maximum of the three
            return max(left_max, right_max, crossing_max)
        
        return find_max_subarray(nums, 0, len(nums) - 1)

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),           # Example 1: [4,-1,2,1]
        ([1], 1),                                        # Example 2: Single element
        ([5, 4, -1, 7, 8], 23),                          # Example 3: Entire array
        ([-1], -1),                                      # Negative single element
        ([-2, -1], -1),                                  # All negative elements
        ([0, 0, 0, 0], 0),                               # All zeros
        ([-2, -3, -1, -5], -1),                          # All negative, return max
        ([3, -2, 5, -1], 6),                             # Multiple subarrays with positive sum
        ([2, 3, -4, 1, 2, -3, 5, -1], 6),                # Various positive and negative
        ([-4, 3, -2, 5, -8, 10, -2, 6], 14),             # Complex case with multiple negative numbers
    ]
    
    print("Testing Kadane's algorithm (iterative):")
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.maxSubArray(nums)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Got {result}, Expected {expected}")
    
    print("\nTesting divide and conquer approach:")
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.maxSubArrayDivideConquer(nums)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Got {result}, Expected {expected}")