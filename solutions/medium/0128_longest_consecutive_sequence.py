from typing import List

class Solution:
    """
    Given an unsorted array of integers nums, return the length of the longest consecutive 
    elements sequence. The algorithm must run in O(n) time.

    Approach:
    - Convert the list to a set to allow O(1) lookups.
    - Iterate over each number in the set.
    - For each number, only start counting if it is the beginning of a sequence 
      (i.e., the previous number is not in the set).
    - Count the length of the consecutive sequence starting from that number.
    - Track and return the maximum sequence length found.

    Time Complexity: O(n) – Each number is processed at most twice.
    Space Complexity: O(n) – Due to storing the set of numbers.
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Convert the list to a set to remove duplicates and for O(1) lookup
        num_set = set(nums)

        # Initialize the longest sequence length
        longest = 0
        
        # Iterate through the set of numbers
        for n in num_set:

            # Only consider starting a new sequence if n is the smallest in the sequence
            if n - 1 not in num_set:

                # Initialize the length of the current sequence 
                length = 1

                # Increment the length of the sequence while the next number is in the set
                while n + length in num_set:
                    length += 1

                # Update the longest sequence length if the current sequence is longer
                longest = max(longest, length)
        
        return longest

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),         # Sequence: [1, 2, 3, 4]
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),   # Sequence: [0, 1, 2, 3, 4, 5, 6, 7, 8]
        ([], 0),                             # No elements
        ([1], 1),                            # Single element
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7)  # Sequence: [3, 4, 5, 6, 7, 8, 9]
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.longestConsecutive(nums)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed.")
