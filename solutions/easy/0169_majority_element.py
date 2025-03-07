from typing import List

class Solution:
    """
    Given an array 'nums' of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times,
    and it is guaranteed to exist in the array.
    
    Approach:
    - This solution uses the Boyer-Moore Voting Algorithm.
    - It maintains a candidate for the majority element and a counter.
    - For each number in the array:
        - If the counter is zero, assign the current number as the new candidate.
        - Increment the counter if the current number matches the candidate,
          otherwise decrement the counter.
    - By the end of the array, the candidate will be the majority element.
    
    Time Complexity: O(n) – We iterate through the array once.
    Space Complexity: O(1) – Only constant extra space is used.
    """
    
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            # If count drops to zero, set a new candidate.
            if count == 0:
                candidate = num
            
            # Increment or decrement the counter.
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([3, 2, 3], 3),               # Majority element is 3.
        ([2, 2, 1, 1, 1, 2, 2], 2),    # Majority element is 2.
        ([1], 1),                     # Only one element, so majority is 1.
        ([1, 1, 2, 1, 3, 1, 4, 1], 1)  # Majority element is 1.
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.majorityElement(nums)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed.")
