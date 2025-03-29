import math
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List
import time

class Solution:
    """
    This class provides methods to estimate the value of π (pi) using random numbers
    drawn from a uniform distribution.
    
    The Monte Carlo method is used, which relies on the relationship between
    the area of a circle (πr²) and the area of a square (4r²) when the circle
    has radius r=1 and is inscribed in a square with side length 2.
    
    The ratio of points falling inside the circle to the total number of points,
    multiplied by 4, gives an approximation of π.
    """
    
    def estimate_pi(self, num_samples: int) -> float:
        """
        Estimate π using the Monte Carlo method with vectorized operations.
        
        Args:
            num_samples (int): Number of random points to generate
            
        Returns:
            float: Estimation of π
            
        Approach:
        - Generate all random points at once using NumPy
        - Calculate all distances in a vectorized operation
        - Count points inside the circle with a single comparison
        
        Time Complexity: O(n) with vectorized operations
        Space Complexity: O(n) as we store all points at once
        """
        if num_samples <= 0:
            raise ValueError("Number of samples must be positive")
        
        # Generate all random points at once
        x = np.random.uniform(-1, 1, num_samples)
        y = np.random.uniform(-1, 1, num_samples)
        
        # Calculate distances in a vectorized operation
        distances_squared = x**2 + y**2
        
        # Count points inside the circle (distance ≤ 1)
        points_in_circle = np.sum(distances_squared <= 1)
        
        # Estimate π
        pi_estimate = 4 * (points_in_circle / num_samples)
        return pi_estimate
    
    def visualize_monte_carlo(self, num_points: int = 1000) -> None:
        """
        Visualize the Monte Carlo method for estimating π using vectorized operations.
        
        Args:
            num_points (int): Number of random points to generate and plot
        """
        # Generate all points at once
        x = np.random.uniform(-1, 1, num_points)
        y = np.random.uniform(-1, 1, num_points)
        
        # Determine which points are inside the circle
        inside_circle = (x**2 + y**2) <= 1
        
        # Plot points
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Points inside the circle
        ax.scatter(x[inside_circle], y[inside_circle], color='blue', alpha=0.6, label='Inside')
        
        # Points outside the circle
        ax.scatter(x[~inside_circle], y[~inside_circle], color='red', alpha=0.6, label='Outside')
        
        # Draw the circle
        circle = plt.Circle((0, 0), 1, fill=False, color='black', linewidth=2)
        ax.add_artist(circle)
        
        # Draw the square
        square = plt.Rectangle((-1, -1), 2, 2, fill=False, color='green', linewidth=2)
        ax.add_artist(square)
        
        # Calculate and display the estimate
        pi_estimate = 4 * np.sum(inside_circle) / num_points
        ax.set_title(f'Monte Carlo Estimation of π\nEstimate: {pi_estimate:.6f}, Actual: {math.pi:.6f}')
        
        ax.set_xlim(-1.1, 1.1)
        ax.set_ylim(-1.1, 1.1)
        ax.set_aspect('equal')
        ax.grid(True)
        ax.legend()
        
        plt.show()

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases with different sample sizes
    test_cases = [
        (100, 0.2),      # Small sample, large error tolerance
        (10000, 0.05),   # Medium sample, medium error tolerance
        (1000000, 0.01)  # Large sample, small error tolerance
    ]
    
    print("Testing Monte Carlo π estimation:")
    for i, (samples, tolerance) in enumerate(test_cases, 1):
        pi_estimate = solution.estimate_pi(samples)
        error = abs(pi_estimate - math.pi)
        within_tolerance = error <= tolerance
        
        print(f"Test {i}: {samples} samples → π ≈ {pi_estimate:.6f}, error: {error:.6f}")
        print(f"  Within tolerance {tolerance}: {within_tolerance}")
    
    # Measure performance with increasing sample sizes
    print("\nPerformance scaling:")
    for samples in [10000, 100000, 1000000, 10000000]:
        start_time = time.time()
        result = solution.estimate_pi(samples)
        elapsed = time.time() - start_time
        print(f"{samples:,} samples: {elapsed:.4f} seconds, π ≈ {result:.6f}")
    
    # Uncomment to visualize (requires matplotlib)
    # solution.visualize_monte_carlo(5000)
