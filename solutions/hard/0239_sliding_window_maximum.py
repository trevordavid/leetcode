from typing import List
from collections import deque

class Solution:
    """
    Given an array of integers 'nums' and an integer 'k', representing the size of a sliding window,
    this function returns a list of the maximum element in each window as it moves from left to right.
    
    Approach:
    - Use a double-ended queue (deque) to store indices of elements in the current window in a way that the 
      largest element's index is always at the front.
    - For each element, remove indices from the back of the deque if their corresponding values are less than
      the current element because they cannot be the maximum.
    - Append the current index.
    - Remove the index at the front if it is outside the current window (i.e., if it is less than i - k + 1).
    - Once the window has reached size 'k' (i.e., i >= k - 1), append the element at the front of the deque to the result.
    
    Time Complexity: O(n) – Each element is added and removed at most once.
    Space Complexity: O(k) – The deque stores indices for at most 'k' elements.
    """
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # Will store indices of elements in 'nums'
        
        for i, num in enumerate(nums):
            # Remove indices from the back whose corresponding values are less than the current element.
            while q and nums[q[-1]] < num:
                q.pop()
            
            # Append the current index.
            q.append(i)
            
            # Remove the index at the front if it's outside the current window.
            if q[0] <= i - k:
                q.popleft()
            
            # Once we've processed at least 'k' elements, add the maximum for the current window.
            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # (nums, k, expected_output)
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([9, 11], 2, [11]),
        ([4, -2], 2, [4]),
    ]
    
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = solution.maxSlidingWindow(nums, k)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed.")
