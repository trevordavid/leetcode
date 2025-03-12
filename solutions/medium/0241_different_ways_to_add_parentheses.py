from typing import List

class Solution:
    def __init__(self):
        # Memoization dictionary to store computed results for sub-expressions
        self.memo = {}

    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
        Given a string expression of numbers and operators, return all possible results from computing
        all the different possible ways to group numbers and operators. You may return the answer in any order.

        :param expression: A string containing numbers and operators ('+', '-', '*')
        :return: A list of all possible results from computing all different possible ways to group numbers and operators
        """
        # If the result for the current expression is already computed, return it
        if expression in self.memo:
            return self.memo[expression]

        results = []

        # Traverse the expression to find operators
        for i, char in enumerate(expression):
            if char in '+-*':
                # Recursively solve for the left and right parts of the expression
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i + 1:])

                # Combine the results from left and right sub-expressions based on the operator
                for left in left_results:
                    for right in right_results:
                        if char == '+':
                            results.append(left + right)
                        elif char == '-':
                            results.append(left - right)
                        elif char == '*':
                            results.append(left * right)

        # Base case: if the expression is a single number, convert it to an integer and add to results
        if not results:
            results.append(int(expression))

        # Store the computed result in the memoization dictionary
        self.memo[expression] = results
        return results

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    expression = "2-1-1"
    expected_output = [0, 2]  # Possible results: (2-(1-1)) = 2, ((2-1)-1) = 0
    assert sorted(solution.diffWaysToCompute(expression)) == sorted(expected_output)
    print(f"Test case 1 passed: {expression} -> {expected_output}")

    # Test case 2
    expression = "2*3-4*5"
    expected_output = [-34, -14, -10, -10, 10]  # Possible results: (2*(3-(4*5))) = -34, ((2*3)-(4*5)) = -14, ((2*(3-4))*5) = -10, (2*((3-4)*5)) = -10, (((2*3)-4)*5) = 10
    assert sorted(solution.diffWaysToCompute(expression)) == sorted(expected_output)
    print(f"Test case 2 passed: {expression} -> {expected_output}")

    # Test case 3
    expression = "3+2*2"
    expected_output = [7, 10]  # Possible results: (3+(2*2)) = 7, ((3+2)*2) = 10
    assert sorted(solution.diffWaysToCompute(expression)) == sorted(expected_output)
    print(f"Test case 3 passed: {expression} -> {expected_output}")

    # Test case 4
    expression = "10"
    expected_output = [10]  # Single number, result is the number itself
    assert sorted(solution.diffWaysToCompute(expression)) == sorted(expected_output)
    print(f"Test case 4 passed: {expression} -> {expected_output}")

    print("All test cases passed.")
