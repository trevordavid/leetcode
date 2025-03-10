from typing import List
from collections import deque

class Solution:
    """
    Given an m x n 2D binary grid 'grid' which represents a map of '1's (land) and '0's (water),
    return the number of islands.
    
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    All four edges of the grid are assumed to be surrounded by water.
    
    Approach:
    - Use breadth-first search (BFS) to traverse the grid.
    - Iterate over each cell of the grid. When a cell with "1" (land) is found, increment the island count 
      and use BFS to mark all adjacent land cells as visited by setting them to "0".
    
    Time Complexity: O(m * n) – Every cell is visited at most once.
    Space Complexity: O(min(m, n)) – The maximum size of the BFS queue in the worst-case scenario.
    """
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"  # Mark as visited
            
            while q:
                row, col = q.popleft()
                # Define the four possible directions: down, up, right, left
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    # Check boundary conditions and if the neighbor is unvisited land ("1")
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"  # Mark as visited
        
        # Iterate over all cells in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        
        return islands

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    import copy
    
    test_cases = [
        # Each test case is a tuple: (grid, expected number of islands)
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ],
            1
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ],
            3
        ),
        (
            [
                ["1", "0", "1", "0", "1"],
                ["0", "1", "0", "1", "0"],
                ["1", "0", "1", "0", "1"],
                ["0", "1", "0", "1", "0"]
            ],
            10
        )
    ]
    
    for i, (grid, expected) in enumerate(test_cases, 1):
        # Use a deep copy since the grid is modified in-place.
        grid_copy = copy.deepcopy(grid)
        result = solution.numIslands(grid_copy)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed: {result} islands found.")
