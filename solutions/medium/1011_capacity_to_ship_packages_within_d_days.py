from typing import List

class Solution:
    """
    A conveyor belt has packages that must be shipped from one port to another within days days.

    The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages 
    on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight 
    capacity of the ship.

    Return the least weight capacity of the ship that will result in all the packages on the conveyor belt 
    being shipped within days days.

    Example:
        Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
        Output: 15
        Explanation: 
            A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
            1st day: 1, 2, 3, 4, 5
            2nd day: 6, 7
            3rd day: 8
            4th day: 9
            5th day: 10

    Example:
        Input: weights = [3,2,2,4,1,4], days = 3
        Output: 6
        Explanation: 
            A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
            1st day: 3, 2
            2nd day: 2, 4
            3rd day: 1, 4
    """
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Find the minimum capacity of the ship to ship all packages within the given days.
        
        Approach:
        - Use binary search to find the minimum capacity
        - The capacity must be at least the maximum weight (lower bound)
        - The capacity at most needs to be the sum of all weights (upper bound)
        - For each capacity, calculate how many days needed and narrow down the search range
        
        Time Complexity: O(n * log(sum(weights))) where n is the length of weights
                       - Binary search takes O(log(sum(weights))) iterations
                       - Each iteration requires O(n) to calculate the days needed
        
        Space Complexity: O(1)
                       - Only a constant amount of extra space is used
        
        Args:
            weights: List of package weights
            days: Maximum number of days allowed for shipping
            
        Returns:
            Minimum capacity of the ship needed
        """
        l = max(weights)  # Capacity must be at least the maximum weight
        r = sum(weights)  # Capacity at most needs to be the sum of all weights

        def shipDays(shipCapacity: int) -> int:
            """Calculate the number of days needed with the given ship capacity."""
            days_needed = 1
            capacity = 0
            for weight in weights:
                if capacity + weight > shipCapacity:
                    days_needed += 1
                    capacity = weight
                else:
                    capacity += weight
            return days_needed

        # Binary search to find the minimum capacity
        while l < r:
            m = (l + r) // 2
            if shipDays(m) <= days:
                r = m
            else:
                l = m + 1

        return l

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([1,2,3,4,5,6,7,8,9,10], 5, 15),            # Example 1
        ([3,2,2,4,1,4], 3, 6),                      # Example 2
        ([1,2,3,4,5,6,7,8,9,10], 10, 10),           # One package per day
        ([1,2,3,4,5,6,7,8,9,10], 1, 55),            # All packages in one day
        ([5,10,15,20,25], 3, 30),                   # Larger weights
        ([1,1,1,1,1], 2, 3),                        # Equal weights
        ([10], 2, 10),                              # Single package
    ]
    
    print("Testing capacity to ship packages within D days:")
    for i, (weights, days, expected) in enumerate(test_cases, 1):
        result = solution.shipWithinDays(weights, days)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Got {result}, Expected {expected}")