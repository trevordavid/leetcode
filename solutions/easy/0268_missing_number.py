from typing import List

class Solution:
    """
    Given an array nums containing n distinct numbers in the range [0, n], 
    return the only number in the range that is missing from the array.
    
    Example:
        Input: nums = [3,0,1]
        Output: 2
        Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
                     2 is the missing number in the range since it does not appear in nums.
    
    Example:
        Input: nums = [0,1]
        Output: 2
        Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
                     2 is the missing number in the range since it does not appear in nums.
    
    Example:
        Input: nums = [9,6,4,2,3,5,7,0,1]
        Output: 8
        Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
                     8 is the missing number in the range since it does not appear in nums.
    """
    
    def missingNumber(self, nums: List[int]) -> int:
        """
        Find the missing number using the sum approach.
        
        Approach:
        - Calculate the expected sum of numbers from 0 to n
        - Calculate the actual sum of numbers in the array
        - The difference is the missing number
        
        Time Complexity: O(n) where n is the length of the array
                       - We iterate through the array once
        
        Space Complexity: O(1) - we only use a constant amount of extra space
        
        Args:
            nums: List of distinct integers in the range [0, n] with one number missing
            
        Returns:
            The missing number in the range
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # Sum of numbers from 0 to n
        actual_sum = sum(nums)           # Sum of numbers in the array
        
        return expected_sum - actual_sum
    
    def missingNumberXOR(self, nums: List[int]) -> int:
        """
        Find the missing number using the XOR approach.
        
        Approach:
        - XOR all numbers from 0 to n with all numbers in the array
        - Since a number XORed with itself results in 0, and any number XORed with 0 is itself,
          the result will be the missing number
        
        Time Complexity: O(n) where n is the length of the array
        Space Complexity: O(1) - we only use a constant amount of extra space
        
        Args:
            nums: List of distinct integers in the range [0, n] with one number missing
            
        Returns:
            The missing number in the range
        """
        result = len(nums)  # Initialize with n
        
        # XOR all numbers from 0 to n-1 with their indices
        for i, num in enumerate(nums):
            result ^= i ^ num
            
        return result
    
    def missingNumberCyclicSort(self, nums: List[int]) -> int:
        """
        Find the missing number using cyclic sort.
        
        Approach:
        - Place each number at its correct index (num at index num)
        - Scan the array to find the index where value doesn't match index
        
        Time Complexity: O(n) where n is the length of the array
        Space Complexity: O(1) - we modify the array in place
        
        Args:
            nums: List of distinct integers in the range [0, n] with one number missing
            
        Returns:
            The missing number in the range
        """
        i = 0
        n = len(nums)
        
        # Place each number at its correct position
        while i < n:
            correct_pos = nums[i]
            
            # If number is n or already at correct position, move to next index
            if correct_pos == n or correct_pos == i:
                i += 1
            else:
                # Swap the number to its correct position
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        
        # Find the missing number by scanning the array
        for i in range(n):
            if nums[i] != i:
                return i
                
        # If all numbers are at correct positions, n is missing
        return n

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([3, 0, 1], 2),                          # Example 1
        ([0, 1], 2),                             # Example 2
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),        # Example 3
        ([0], 1),                                # Single element array
        ([1], 0),                                # Missing first element
        ([0, 1, 2, 3, 4, 6], 5),                 # Missing middle element
        ([0, 1, 3], 2),                          # Small array
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 0),        # Missing zero
    ]
    
    print("Testing sum approach:")
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.missingNumber(nums.copy())
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Got {result}, Expected {expected}")
    
    print("\nTesting XOR approach:")
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.missingNumberXOR(nums.copy())
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Got {result}, Expected {expected}")
    
    print("\nTesting cyclic sort approach:")
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.missingNumberCyclicSort(nums.copy())
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Got {result}, Expected {expected}")
