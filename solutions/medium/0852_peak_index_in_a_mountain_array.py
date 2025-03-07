from typing import List

class Solution:
    """
    Given a mountain array 'arr', where the values first increase to a peak and then decrease,
    return the index of the peak element. The solution is designed to run in O(log(n)) time.
    
    Approach:
    - Use binary search to efficiently locate the peak.
    - Initialize two pointers, 'low' and 'high'.
    - Compute the middle index 'mid' using low + (high - low) // 2.
    - If arr[mid] is less than arr[mid + 1], it indicates that the peak is to the right,
      so update low to mid + 1.
    - Otherwise, the peak is at mid or to the left, so update high to mid.
    - Continue until low equals high, at which point low (or high) is the index of the peak.
    
    Time Complexity: O(log(n)) – The search space is halved in every iteration.
    Space Complexity: O(1) – Only constant extra space is used.
    """
    
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            # If the middle element is less than its right neighbor,
            # then the peak must be to the right.
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                # Else, the peak is at mid or to the left.
                high = mid
                
        # When low equals high, we've found the peak index.
        return low

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([0, 1, 0], 1),              # Peak at index 1
        ([0, 2, 1, 0], 1),           # Peak at index 1
        ([0, 5, 10, 7, 4, 1], 2),     # Peak at index 2
        ([3, 8, 12, 10, 5, 2], 2),     # Peak at index 2
        ([1, 3, 5, 7, 6, 4, 2], 3),   # Peak at index 3
    ]
    
    for i, (arr, expected) in enumerate(test_cases, 1):
        result = solution.peakIndexInMountainArray(arr)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed.")
