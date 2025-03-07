from typing import List

class Solution:
    """
    There is a robot on an m x n grid. The robot is initially located at the top-left corner 
    (i.e., grid[0][0]). It aims to move to the bottom-right corner (i.e., grid[m - 1][n - 1]) and 
    can only move either down or right at any point in time.
    
    Given two integers, m and n, this function returns the number of unique paths the robot can take 
    to reach the bottom-right corner.
    
    The test cases are generated so that the answer will be less than or equal to 2 * 10^9.
    
    Key Insight:
    - The number of unique paths to reach a cell is the sum of the number of unique paths to reach the cell above it and the cell to its left.

    Approach:
    - Use dynamic programming to compute the number of ways to reach each cell.
    - Instead of using a full m x n matrix, maintain only a single row ("aboveRow") to represent the 
      previous row’s results.
    - For each new row, initialize a current row with ones (as the first cell is always reachable in 1 way).
    - For every subsequent cell in the current row, update it as the sum of the value to its left and 
      the value from the same column in the previous row.
      
    Time Complexity: O(m × n) – each cell in the grid is processed once.
    Space Complexity: O(n) – only one row (and a temporary row) is stored at any time.
    """
    
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the first row; there's only one way to reach any cell in the top row.
        aboveRow = [1] * n

        # Process each subsequent row.
        for _ in range(m - 1):
            currentRow = [1] * n
            # Update cells starting from the second column.
            for i in range(1, n):
                currentRow[i] = currentRow[i - 1] + aboveRow[i]
            # Prepare for next iteration by updating aboveRow.
            aboveRow = currentRow

        return aboveRow[-1]

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ((3, 7), 28),  # For a 3x7 grid, there are 28 unique paths.
        ((3, 2), 3),   # For a 3x2 grid, there are 3 unique paths.
        ((7, 3), 28),  # For a 7x3 grid, there are 28 unique paths.
        ((3, 3), 6),   # For a 3x3 grid, there are 6 unique paths.
        ((1, 1), 1),   # A 1x1 grid has only 1 path (start is finish).
    ]
    
    for i, ((m, n), expected) in enumerate(test_cases, 1):
        result = solution.uniquePaths(m, n)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed.")
