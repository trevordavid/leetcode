from typing import List
import heapq

class Solution:
    """
    Given an integer array, this function returns the maximum product of any three
    numbers in the array.
    
    There are two possible scenarios for maximum product:
    1. Product of the three largest numbers (for all positive or all negative cases)
    2. Product of the two smallest numbers and the largest number (when we have negatives)
    
    Approach:
    - Sort the array
    - Calculate both: (three largest numbers) and (two smallest and the largest)
    - Return the maximum product
    
    Time Complexity: O(n log n) where n is the length of the array (due to sorting)
    Space Complexity: O(1) as we only use a constant amount of extra space
    """
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            raise ValueError("Array must have at least 3 elements")
            
        # Sort the array
        nums.sort()
        
        # Two cases to consider:
        # 1. The three largest numbers (from the end of the sorted array)
        # 2. The two smallest numbers (which could be negative) and the largest number
        
        # Case 1: Three largest numbers
        max_product1 = nums[-1] * nums[-2] * nums[-3]
        
        # Case 2: Two smallest numbers and the largest number
        max_product2 = nums[0] * nums[1] * nums[-1]
        
        # Return the maximum of the two products
        return max(max_product1, max_product2)


    def maximumProductHeap(self, nums: List[int]) -> int:
        """
        Implementation using heaps to find the 3 largest and 2 smallest elements.
        This approach reduces time complexity to O(n) since finding k largest/smallest 
        elements in a heap is O(n + k log n), and here k is a constant (2 or 3).
        
        Time Complexity: O(n)
        Space Complexity: O(1) as we only store a constant number of elements
        """
        if len(nums) < 3:
            raise ValueError("Array must have at least 3 elements")
            
        a = heapq.nlargest(3, nums)
        b = heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])
    
    def maximumProductLinear(self, nums: List[int]) -> int:
        """
        Single-pass O(n) approach that tracks the 3 largest and 2 smallest elements.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(nums) < 3:
            raise ValueError("Array must have at least 3 elements")
            
        # Initialize with extreme values
        max1 = max2 = max3 = float('-inf')  # Three largest
        min1 = min2 = float('inf')          # Two smallest
        
        for num in nums:
            # Update three largest elements
            if num > max1:
                max3, max2, max1 = max2, max1, num
            elif num > max2:
                max3, max2 = max2, num
            elif num > max3:
                max3 = num
                
            # Update two smallest elements
            if num < min1:
                min2, min1 = min1, num
            elif num < min2:
                min2 = num
        
        # Return max of the two products
        return max(max1 * max2 * max3, min1 * min2 * max1)

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([1, 3, 4, 5], 60),                # Example A: 3*4*5 = 60
        ([-2, -4, 5, 3], 40),               # Example B: -2*-4*5 = 40
        ([1, 2, 3], 6),                     # Only 3 elements
        ([-1, -2, -3, -4], -6),             # All negative
        ([-10, -10, 1, 2, 3], 300),         # Two large negatives, one positive
        ([1000, 1000, -1, -1, -1000], 1000000), # Two large positives, one large negative
        ([0, 0, 0, 1], 0),                  # Contains zeros
        ([-5, -2, -1, 0, 1], 10),           # Mix of negatives, zero and positives
    ]
    
    # Test the sort-based implementation
    print("Testing sort-based implementation:")
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.maximumProduct(nums)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed: {nums} -> {result}")
    
    # Test the heap-based implementation
    print("\nTesting heap-based implementation:")
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.maximumProductHeap(nums)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed: {nums} -> {result}")
        
    # Test the linear-time implementation
    print("\nTesting linear-time implementation:")
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.maximumProductLinear(nums)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed: {nums} -> {result}")
