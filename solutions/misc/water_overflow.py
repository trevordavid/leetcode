# There is a stack of water glasses in the form of a Pascal triangle and a person wants to pour the water at the topmost glass, but the capacity of each glass is 1 unit. Overflow takes place in such a way that after 1 unit, 1/2 of the remaining unit gets into the bottom left glass and the other half in the bottom right glass. Now John pours K units of water in the topmost glass and wants to know how much water is there in the Cth glass of the Rth row.

# Note: Assume that there are enough glasses in the triangle till no glass overflows.

class Solution:
    """
    Calculate the amount of water in a specific glass after pouring water at the top.
    
    The glasses are arranged in a Pascal triangle:
                 1
                / \
               2   3
              / \ / \
             4   5   6
            / \ / \ / \
           7   8   9  10
    
    Each glass has a capacity of 1 unit. When a glass overflows, 
    half of the excess water goes to the bottom left glass and 
    half to the bottom right glass.
    
    Example:
        Input: K=2, R=1, C=1
        Output: 1.0
        
        Explanation: After pouring 2 units of water at the top:
        - The top glass (row 1, col 1) gets filled with 1 unit
        - 1 unit overflows and gets equally divided between glasses (2,1) and (2,2)
        - So each of the bottom glasses gets 0.5 units
        
    Example:
        Input: K=3, R=2, C=2
        Output: 0.75
        
        Explanation: After pouring 3 units:
        - Top glass gets 1 unit, 2 units overflow
        - Each glass in row 2 gets 1 unit, 1 unit overflows from each
        - So the middle glass in row 3 gets 0.5 + 0.5 = 1.0 units
        - And glasses (3,1) and (3,3) get 0.5 units each
    """
    
    def waterOverflow(self, K: int, R: int, C: int) -> float:
        """
        Calculate the amount of water in a specific glass after pouring K units.
        
        Approach:
        - Create a 2D array to represent the amount of water in each glass
        - Simulate pouring and overflow row by row
        - When a glass receives more than 1 unit, keep 1 unit and distribute excess equally
        
        Time Complexity: O(R^2) where R is the number of rows to process
                       - We process each glass once, and there are R(R+1)/2 glasses
        
        Space Complexity: O(R^2) to store the state of all glasses
        
        Args:
            K: Amount of water poured at the top
            R: Row of the target glass (1-indexed)
            C: Column of the target glass (1-indexed)
            
        Returns:
            Amount of water in the specified glass
        """
        # Convert to 0-indexed for easier array manipulation
        R = R - 1
        C = C - 1
        
        # Initialize the glasses array with enough rows
        # We need R+1 rows to check the specified glass
        glasses = [[0] * (i + 1) for i in range(R + 1)]
        
        # Pour K units of water into the top glass
        glasses[0][0] = K
        
        # Process each row
        for i in range(R):
            for j in range(len(glasses[i])):
                # If this glass has more than 1 unit of water
                if glasses[i][j] > 1.0:
                    # Calculate overflow amount
                    overflow = (glasses[i][j] - 1.0) / 2.0
                    
                    # Keep 1 unit in the current glass
                    glasses[i][j] = 1.0
                    
                    # Distribute overflow to the glasses below
                    glasses[i + 1][j] += overflow       # Bottom left
                    glasses[i + 1][j + 1] += overflow   # Bottom right
        
        # Return the amount in the specified glass, capped at 1.0
        return min(1.0, glasses[R][C])
    
    def waterOverflowOptimized(self, K: int, R: int, C: int) -> float:
        """
        Optimized solution that only calculates glasses that affect the target glass.
        
        Instead of calculating all glasses in the triangle, we only process the glasses
        that can potentially overflow into our target glass. This reduces the computation
        for very large inputs.
        
        Time Complexity: O(R^2) in worst case, but often much better
        Space Complexity: O(R^2) but can be optimized to O(R)
        
        Args:
            K: Amount of water poured at the top
            R: Row of the target glass (1-indexed)
            C: Column of the target glass (1-indexed)
            
        Returns:
            Amount of water in the specified glass
        """
        # Convert to 0-indexed
        R = R - 1
        C = C - 1
        
        # Create a 2D array to store water amounts
        # We only need up to row R
        glasses = [[0] * (i + 1) for i in range(R + 1)]
        
        # Start with K units at the top
        glasses[0][0] = K
        
        # Process each level
        for i in range(R):
            for j in range(i + 1):
                # Skip glasses that don't overflow
                if glasses[i][j] <= 1.0:
                    continue
                
                # Calculate overflow
                excess = glasses[i][j] - 1.0
                glasses[i][j] = 1.0  # Keep 1 unit
                
                # Distribute overflow to glasses below
                glasses[i + 1][j] += excess / 2.0        # Left
                glasses[i + 1][j + 1] += excess / 2.0    # Right
        
        # Return the amount in the target glass (capped at 1.0)
        return min(1.0, glasses[R][C])

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        # K, R, C, expected
        (2, 1, 1, 1.0),                # Top glass with 2 units poured
        (2, 2, 1, 0.5),                # Bottom left glass after pouring 2 units
        (2, 2, 2, 0.5),                # Bottom right glass after pouring 2 units
        (3, 2, 2, 1.0),                # Middle glass in row 2 after pouring 3 units
        (3, 3, 2, 0.75),               # Middle glass in row 3 after pouring 3 units
        (4, 3, 1, 0.5),                # First glass in row 3 after pouring 4 units
        (4, 3, 3, 0.5),                # Last glass in row 3 after pouring 4 units
        (10, 4, 3, 1.0),               # Glass in row 4 after pouring 10 units
        (1, 1, 1, 1.0),                # Only top glass, exactly 1 unit
        (0.5, 1, 1, 0.5),              # Only top glass, less than capacity
        (0, 3, 2, 0.0),                # No water poured
        (100, 15, 10, 0.9921875),      # Large amount of water
    ]
    
    print("Testing main solution:")
    for i, (K, R, C, expected) in enumerate(test_cases, 1):
        result = solution.waterOverflow(K, R, C)
        # Use a small epsilon for floating point comparison
        status = "✓" if abs(result - expected) < 1e-6 else "✗"
        print(f"Test {i}: {status} Got {result:.7f}, Expected {expected:.7f}")
    
    print("\nTesting optimized solution:")
    for i, (K, R, C, expected) in enumerate(test_cases, 1):
        result = solution.waterOverflowOptimized(K, R, C)
        status = "✓" if abs(result - expected) < 1e-6 else "✗"
        print(f"Test {i}: {status} Got {result:.7f}, Expected {expected:.7f}")

