from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Given an array of intervals where intervals[i] = [start_i, end_i],
        merge all overlapping intervals, and return an array of the non-overlapping
        intervals that cover all the intervals in the input.
        """
        if not intervals:
            return []

        # Sort intervals based on the starting times
        intervals.sort(key=lambda x: x[0])

        merged_intervals = [intervals[0]]

        for current in intervals[1:]:
            last_merged = merged_intervals[-1]

            # If the current interval overlaps with the last merged interval, merge them
            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # Otherwise, add the current interval to the merged list
                merged_intervals.append(current)

        return merged_intervals

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),  # Overlapping intervals
        ([[1, 4], [4, 5]], [[1, 5]]),  # Adjacent intervals
        ([[1, 4], [5, 6]], [[1, 4], [5, 6]]),  # Non-overlapping intervals
        ([[1, 4], [2, 3]], [[1, 4]]),  # Completely overlapping intervals
        ([[1, 4]], [[1, 4]]),  # Single interval
        ([], []),  # Empty list
    ]

    solution = Solution()
    for i, (intervals, expected_output) in enumerate(test_cases, 1):
        result = solution.merge(intervals)
        assert result == expected_output, f"Test case {i} failed: Expected {expected_output}, got {result}"
        print(f"Test case {i} passed: {result}")
