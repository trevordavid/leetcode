from typing import List
from collections import defaultdict

class Solution:
    """
    A class for finding Ramanujan numbers (taxicab numbers).
    
    A Ramanujan number is a positive integer that can be expressed as the sum of two 
    positive cubes in at least two different ways. The most famous example is 1729:
    1729 = 1³ + 12³ = 9³ + 10³
    
    This was noted by mathematician G.H. Hardy when visiting Srinivasa Ramanujan in the hospital.
    Hardy mentioned he had come in taxi number 1729, which seemed a rather dull number.
    Ramanujan immediately responded that 1729 was actually quite interesting - it was the 
    smallest number expressible as the sum of two cubes in two different ways.
    """
    
    def first_n_ramanujan_numbers(self, n: int) -> List[int]:
        """
        Find the first n Ramanujan numbers (taxicab numbers).
        
        Approach:
        - Generate all possible sums of two cubes up to a reasonable limit
        - Store them in a dictionary with the sum as key and list of cube pairs as value
        - Filter for sums that have at least two different pairs of cubes
        - Sort and return the first n such numbers
        
        Args:
            n (int): The number of Ramanujan numbers to find
            
        Returns:
            List[int]: The first n Ramanujan numbers in ascending order
            
        Time Complexity: O(m²) where m is the upper bound of our search space
        Space Complexity: O(m²) to store all possible sums
        """
        if n <= 0:
            return []
        
        # We'll start with a reasonable upper bound for the cube root
        # For the first few Ramanujan numbers, a limit of 100 is more than enough
        limit = 100
        
        # Dictionary to store sums of cubes
        # Key: sum of two cubes
        # Value: list of pairs (a, b) where a³ + b³ equals the key
        sums_of_cubes = defaultdict(list)
        
        # Generate all possible sums of two cubes
        for a in range(1, limit):
            a_cubed = a**3
            for b in range(a, limit):  # Start from a to avoid duplicates like (a,b) and (b,a)
                b_cubed = b**3
                total = a_cubed + b_cubed
                sums_of_cubes[total].append((a, b))
        
        # Find sums that can be expressed as the sum of two cubes in at least two different ways
        ramanujan_numbers = []
        for total, pairs in sums_of_cubes.items():
            if len(pairs) >= 2:
                ramanujan_numbers.append(total)
        
        # Sort the numbers and return the first n
        ramanujan_numbers.sort()
        return ramanujan_numbers[:n]

    def verify_ramanujan_number(self, num: int) -> bool:
        """
        Verify if a number is a Ramanujan number by finding if it can be expressed
        as the sum of two cubes in at least two different ways.
        
        Args:
            num (int): The number to check
            
        Returns:
            bool: True if the number is a Ramanujan number, False otherwise
        """
        pairs = []
        # Upper bound for the cube root search
        limit = int(num**(1/3)) + 1
        
        for a in range(1, limit):
            a_cubed = a**3
            if a_cubed >= num:
                break
                
            # Check if (num - a³) is a perfect cube
            remainder = num - a_cubed
            b = round(remainder**(1/3))
            
            # Verify if b³ + a³ = num
            if b >= a and a_cubed + b**3 == num:
                pairs.append((a, b))
                
        # It's a Ramanujan number if we found at least two different pairs
        return len(pairs) >= 2

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    # Test finding the first n Ramanujan numbers
    test_cases = [
        (1, [1729]),               # The first Ramanujan number
        (2, [1729, 4104]),         # The first two Ramanujan numbers
        (3, [1729, 4104, 13832]),  # The first three Ramanujan numbers
        (5, [1729, 4104, 13832, 20683, 32832]),  # The first five Ramanujan numbers
        (0, []),                   # Edge case: n = 0
    ]
    
    print("Testing first_n_ramanujan_numbers:")
    for i, (n, expected) in enumerate(test_cases, 1):
        result = solution.first_n_ramanujan_numbers(n)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed: first {n} Ramanujan numbers -> {result}")
    
    # Test verification of individual Ramanujan numbers
    verification_tests = [
        (1729, True),   # 1³ + 12³ = 9³ + 10³
        (4104, True),   # 2³ + 16³ = 9³ + 15³
        (13832, True),  # 2³ + 24³ = 18³ + 20³
        (1000, False),  # Not a Ramanujan number
        (728, False),   # Not a Ramanujan number
    ]
    
    print("\nTesting verify_ramanujan_number:")
    for i, (num, expected) in enumerate(verification_tests, 1):
        result = solution.verify_ramanujan_number(num)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed: {num} is a Ramanujan number -> {result}")
