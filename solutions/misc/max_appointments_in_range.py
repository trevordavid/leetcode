from typing import List

class Solution:
    """
    Given a list of appointment times and a time range k, this function returns the maximum 
    number of appointments that can be accommodated within any k-minute window.
    
    Approach:
    - Sort the appointment times to ensure chronological order
    - Use a sliding window technique to find the maximum number of appointments
    - For each end position, adjust the start position to maintain window size <= k
    - Keep track of the maximum number of appointments found in any valid window
    
    Time Complexity: O(n log n) where n is the number of appointments
                   - O(n log n) for sorting
                   - O(n) for the sliding window
    Space Complexity: O(1) as we only use a constant amount of extra space
    """
    def maxAppointmentsInRange(self, appointments: List[int], k: int) -> int:
        # Sort the appointment times
        appointments.sort()
        
        max_count = 0
        start = 0
        
        # Use a sliding window approach
        for end in range(len(appointments)):
            # Expand the window by moving the end pointer
            while appointments[end] - appointments[start] > k:
                # Shrink the window from the start if the range exceeds k
                start += 1
            # Calculate the number of appointments in the current window
            current_count = end - start + 1
            # Update max_count if the current window has more appointments
            max_count = max(max_count, current_count)
        
        return max_count

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([2, 4, 25, 2, 5, 4, 8, 3, 24, 9, 9, 2, 2], 4, 8),     # Original example
        ([1, 2, 3, 4, 5], 2, 3),                                # Sequential appointments
        ([1, 5, 10, 15, 20], 5, 2),                            # No overlapping appointments
        ([1, 1, 1, 1, 1], 1, 5),                               # All appointments at same time
        ([], 5, 0),                                             # Empty list
        ([1, 2, 3, 4, 5], 10, 5),                              # All appointments in range
    ]
    
    for i, (appointments, k, expected) in enumerate(test_cases, 1):
        result = solution.maxAppointmentsInRange(appointments, k)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed: appointments={appointments}, k={k} -> {result}")
