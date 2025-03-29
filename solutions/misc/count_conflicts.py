from typing import List, Tuple

class Solution:
    """
    Determine the number of room conflicts from a list of start and end-time tuples.
    A conflict occurs when the number of concurrent intervals exceeds the maximum number
    of available rooms. Each time an interval starts when all rooms are occupied,
    it counts as a new conflict.
    
    For example, with max_rooms = 2:
    - First interval: no conflict (1 room used)
    - Second interval: no conflict (2 rooms used)
    - Third interval overlaps: 1 conflict (exceeds capacity)
    - Fourth interval overlaps: 1 more conflict (exceeds capacity)
    
    Approach:
    - Convert each interval into two events: start and end
    - Sort events by time (with end events processed before start events at same time)
    - Use a sweep line algorithm to track the number of active intervals
    - When active intervals exceed max_rooms, count it as a conflict
    
    Time Complexity: O(n log n) where n is the number of intervals
                   - O(n log n) for sorting the events
                   - O(n) for processing the events
    Space Complexity: O(n) for storing the events array
    """
    def countConflicts(self, intervals: List[Tuple[int, int]], max_rooms: int) -> int:
        if not intervals:
            return 0
            
        # Create a list to hold all events
        events = []
        for start, end in intervals:
            events.append((start, 1))  # 1 for start (lower priority)
            events.append((end, 0))    # 0 for end (higher priority)
        
        # Sort events by time, with end events coming before start events at same time
        events.sort()
        
        current_rooms = 0
        conflicts = 0
        
        # Process all events
        for _, event_type in events:
            if event_type == 1:  # Start event
                current_rooms += 1
                if current_rooms > max_rooms:
                    conflicts += 1
            else:  # End event
                current_rooms -= 1
        
        return conflicts

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # (intervals, max_rooms, expected_conflicts)
        ([(1, 5), (3, 7), (2, 6), (10, 15), (5, 6), (4, 100)], 2, 3),  # Original example with 2 rooms
        ([(1, 2), (2, 3), (3, 4)], 1, 0),                               # No overlapping intervals
        ([(1, 5), (1, 5), (1, 5)], 2, 1),                               # 3 identical intervals, 2 rooms
        ([(1, 2), (1, 2), (1, 2), (1, 2)], 2, 2),                      # 4 identical intervals, 2 rooms
        ([], 1, 0),                                                      # Empty list
        ([(1, 10), (2, 8), (3, 6), (4, 4)], 2, 2),                     # Nested intervals, 2 rooms
        ([(1, 5), (2, 3), (2, 4)], 1, 2),                              # Multiple overlaps, 1 room
    ]
    
    for i, (intervals, max_rooms, expected) in enumerate(test_cases, 1):
        result = solution.countConflicts(intervals, max_rooms)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed: intervals={intervals}, max_rooms={max_rooms} -> {result}")
