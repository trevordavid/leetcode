from typing import List

class Solution:
    """
    There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

    The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

    The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

    Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
    
    Approach:
    - Use depth-first search (DFS) from each ocean's boundary to "spread" inward.
    - For each boundary cell, DFS is performed to mark all cells that can be reached following the rule 
      that water can only flow from a cell to another if the next cell's height is greater than or equal 
      to the previous cell's height.
    - Pacific is reached from the top row and left column, while Atlantic is reached from the bottom row 
      and right column.
    - The final result is the intersection of the cells reachable from both oceans.
    
    Time Complexity: O(m * n) – Each cell is visited at most once.
    Space Complexity: O(m * n) – For the recursion stack and visited sets.
    """
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
        
        def dfs(visited, row, col, prev_height):
            # Check for grid boundaries.
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            
            # Skip if this cell is already visited.
            if (row, col) in visited:
                return
            
            # Only proceed if the current cell's height is at least the height of the previous cell,
            # ensuring that water can flow from the previous cell to the current cell.
            if heights[row][col] < prev_height:
                return
            
            # Mark the cell as visited for the current ocean.
            visited.add((row, col))
            
            # Explore all four directions.
            dfs(visited, row + 1, col, heights[row][col])
            dfs(visited, row - 1, col, heights[row][col])
            dfs(visited, row, col + 1, heights[row][col])
            dfs(visited, row, col - 1, heights[row][col])
        
        # Start DFS from the Pacific boundaries: top row and left column.
        for col in range(cols):
            dfs(pacific_visited, 0, col, heights[0][col])         # Top row.
            dfs(atlantic_visited, rows - 1, col, heights[rows - 1][col])  # Bottom row for Atlantic.
        for row in range(rows):
            dfs(pacific_visited, row, 0, heights[row][0])           # Left column.
            dfs(atlantic_visited, row, cols - 1, heights[row][cols - 1])   # Right column.
        
        # The final result is the intersection of cells reachable by both oceans.
        return [list(cell) for cell in (pacific_visited & atlantic_visited)]

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # Test Case 1
        (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4]
            ],
            # Expected output (order of coordinates may vary):
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        ),
        # Test Case 2: A grid where all boundary cells are high, so every boundary cell flows to both oceans.
        (
            [
                [10, 10, 10],
                [10,  1, 10],
                [10, 10, 10]
            ],
            [[0, 0], [0, 1], [0, 2],
             [1, 0],         [1, 2],
             [2, 0], [2, 1], [2, 2]]
        )
    ]
    
    def sort_coords(coords):
        return sorted(coords, key=lambda x: (x[0], x[1]))
    
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.pacificAtlantic(heights)
        # Compare sorted results for consistency.
        if sort_coords(result) != sort_coords(expected):
            raise AssertionError(f"Test case {i} failed: Expected {expected}, got {result}")
        print(f"Test case {i} passed: {result}")
