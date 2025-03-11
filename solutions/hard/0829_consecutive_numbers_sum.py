class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        """
        Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.
        """
        count = 0  # Initialize the count of possible ways

        # Iterate over possible lengths of consecutive sequences
        for k in range(1, n):
            # Calculate the starting number x for the sequence of length k+1
            x = n / (k + 1) - k / 2

            # If x is less than or equal to 0, further sequences will not be valid
            if x <= 0:
                break

            # Check if x is an integer
            if x == int(x):
                count += 1

        # Include the number itself as a valid sequence
        return count + 1

# Test cases to validate the solution
def run_tests():
    solution = Solution()
    test_cases = [
        (5, 2),   # 5 = 5 or 2 + 3
        (9, 3),   # 9 = 9 or 4 + 5 or 2 + 3 + 4
        (15, 4),  # 15 = 15 or 7 + 8 or 4 + 5 + 6 or 1 + 2 + 3 + 4 + 5
        (1, 1),   # 1 = 1
        (3, 2),   # 3 = 3 or 1 + 2
        (10, 2),  # 10 = 10 or 1 + 2 + 3 + 4
    ]
    for n, expected in test_cases:
        result = solution.consecutiveNumbersSum(n)
        assert result == expected, f"Test failed for n={n}: expected {expected}, got {result}"
    print("All tests passed.")

run_tests()
