class Solution:
    """
    Find equilibrium points in a linear array of magnets.
    
    Problem: N magnets are placed on a line. Each magnet experiences repulsive 
    forces from other magnets, with force = 1/d where d is the distance.
    We need to find all points where the net force is ZERO (equilibrium points).
    
    Since magnets repel each other, there is exactly one equilibrium point 
    between each adjacent pair of magnets, giving N-1 total equilibrium points.
    
    Note: Input array M[] is sorted and results should have 2 decimal precision.
    """
    def calculate_net_force(self, position, magnets, n):
        """
        Calculate the net force at a given position due to all magnets.
        
        Args:
            position: X-coordinate to calculate force at
            magnets: Array of magnet positions
            n: Number of magnets
            
        Returns:
            Net force at the given position (positive = rightward, negative = leftward)
        """
        # Force from magnets to the left (pushing right, positive force)
        left_force = sum(1 / (position - magnets[i]) for i in range(n) if magnets[i] < position)
        
        # Force from magnets to the right (pushing left, negative force)
        right_force = sum(1 / (magnets[i] - position) for i in range(n) if magnets[i] > position)
        
        return left_force - right_force
    
    def should_move_right(self, force):
        """
        Determine which direction to move in binary search based on force.
        
        Args:
            force: Net force at current position
            
        Returns:
            True if should move right, False if should move left
        """
        return force > 0  # If net force is positive (rightward), move right
    
    def find_equilibrium(self, left_bound, right_bound, magnets, n):
        """
        Binary search to find equilibrium point with precision 1e-6.
        
        Args:
            left_bound: Left boundary for binary search (magnet position)
            right_bound: Right boundary for binary search (next magnet position)
            magnets: Array of magnet positions
            n: Number of magnets
            
        Returns:
            X-coordinate of equilibrium point with 2 decimal precision
        """
        left = left_bound
        right = right_bound
        
        while right - left > 1e-9:  # High precision to ensure 2 decimal places
            mid = (left + right) / 2
            force = self.calculate_net_force(mid, magnets, n)
            
            if self.should_move_right(force):
                left = mid  # Move right if net force is positive
            else:
                right = mid  # Move left if net force is negative or zero
                
        # Return the midpoint rounded to 2 decimal places
        return round((left + right) / 2, 2)
    
    def nullPoints(self, n, M, getAnswer):
        """
        Find all N-1 equilibrium points between N magnets.
        
        Args:
            n: Number of magnets
            M: Array of magnet positions (sorted)
            getAnswer: Array to store the equilibrium points
            
        Returns:
            None (results stored in getAnswer array)
        """
        # Finding N-1 equilibrium points between each pair of adjacent magnets
        for i in range(n - 1):
            getAnswer[i] = self.find_equilibrium(M[i], M[i + 1], M, n)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # Simple test case with 3 magnets
        [1, 2, 5],
        
        # Evenly spaced magnets
        [0, 10, 20, 30, 40],
        
        # Magnets with varying distances
        [0, 2, 6, 18, 20]
    ]
    
    for i, magnets in enumerate(test_cases):
        n = len(magnets)
        result = [0] * (n - 1)  # Array to store equilibrium points
        solution.nullPoints(n, magnets, result)
        
        print(f"Test Case {i+1}:")
        print(f"Magnets: {magnets}")
        print(f"Equilibrium points: {result}")
        print()
        
        # Verification: Calculate net force at equilibrium points (should be close to zero)
        for j, point in enumerate(result):
            force = solution.calculate_net_force(point, magnets, n)
            print(f"  Point {j+1}: {point}, Net Force: {force:.10f}")
        print("-------------------")
