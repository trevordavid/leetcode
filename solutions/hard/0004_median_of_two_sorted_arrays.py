from typing import List

class Solution:
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively, 
    this function returns the median of the two sorted arrays.
    
    The median of a sorted array is:
    - For an array with odd length, the middle element
    - For an array with even length, the average of the two middle elements
    
    The problem requires O(log(m+n)) time complexity.
    """
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of two sorted arrays using the binary search approach.
        
        Approach:
        - Use binary search to find the partition that divides the combined array into two equal halves
        - Ensure elements on the left side are smaller than elements on the right side
        - The median is determined from the elements at the partition boundaries
        
        Time Complexity: O(log(min(m,n))) where m and n are the lengths of the arrays
        Space Complexity: O(1) as we only use a constant amount of extra space
        
        Args:
            nums1 (List[int]): First sorted array
            nums2 (List[int]): Second sorted array
            
        Returns:
            float: The median of the combined sorted arrays
        """
        # Ensure nums1 is the smaller array for efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            # Partition the smaller array (nums1)
            partitionX = (low + high) // 2
            # Calculate the corresponding partition in nums2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # Get the elements around the partition
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]
            
            # Check if we found the correct partition
            if maxX <= minY and maxY <= minX:
                # If total length is odd, median is the maximum of left elements
                if (x + y) % 2 != 0:
                    return max(maxX, maxY)
                # If total length is even, median is average of max of left and min of right
                else:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
            # Adjust the partition
            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1
        
        # If we reach here, the arrays are not sorted correctly
        raise ValueError("Input arrays are not sorted correctly")
    
    def findMedianSortedArrays_simple(self, nums1: List[int], nums2: List[int]) -> float:
        """
        A simple approach to find the median of two sorted arrays by merging them.
        
        This is NOT the optimal solution, as it has a time complexity of O((m+n)log(m+n)).
        
        Approach:
        - Merge the two arrays
        - Sort the merged array
        - Find the median based on the length of the merged array
        
        Time Complexity: O((m+n)log(m+n)) due to sorting
        Space Complexity: O(m+n) for storing the merged array
        
        Args:
            nums1 (List[int]): First sorted array
            nums2 (List[int]): Second sorted array
            
        Returns:
            float: The median of the combined sorted arrays
        """
        # Merge the arrays
        merge = nums1 + nums2
        # Sort the merged array
        merge.sort()
        
        n = len(merge)
        
        # Find the median
        # If the total number of elements is odd, return the middle element
        if n % 2 != 0:
            return merge[n // 2]
        # If the total number of elements is even, return the average of the two middle elements
        else:
            return (merge[n // 2] + merge[n // 2 - 1]) / 2

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([1, 3], [2], 2.0),                          # Odd total length
        ([1, 2], [3, 4], 2.5),                       # Even total length
        ([0, 0], [0, 0], 0.0),                       # Same elements
        ([], [1], 1.0),                              # One empty array
        ([], [2, 3], 2.5),                           # One empty array, even length
        ([1, 3, 5, 7], [2, 4, 6, 8], 4.5),           # Multiple elements, even total
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5.5),    # No overlap
        ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 5.5),    # Interleaved elements
        ([1, 2], [1, 2, 3], 2.0),                    # Overlapping elements, mixed length
        ([1, 2, 3], [4, 5, 6, 7, 8], 4.5)            # Different lengths (corrected expected value)
    ]
    
    print("Testing findMedianSortedArrays (optimal solution):")
    for i, (nums1, nums2, expected) in enumerate(test_cases, 1):
        result = solution.findMedianSortedArrays(nums1, nums2)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed: nums1={nums1}, nums2={nums2} -> {result}")
    
    print("\nVerifying with simple solution:")
    for i, (nums1, nums2, expected) in enumerate(test_cases, 1):
        result = solution.findMedianSortedArrays_simple(nums1, nums2)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed: nums1={nums1}, nums2={nums2} -> {result}")
