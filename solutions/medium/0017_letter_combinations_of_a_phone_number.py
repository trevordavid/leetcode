
from typing import List

class Solution:
    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order. A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
 
    Approach:
    - Use backtracking to explore all possible combinations.
    - For each digit, iterate through its mapped letters and add them one by one to the current combination.
    - Once the combination length equals the input digits length, add the combination to the result list.
    
    Time Complexity:  O(3^n) or O(4^n) in the worst case, where n is the length of digits (each digit can map to up to 4 letters).
    Space Complexity: O(n) for the recursion stack.
    """
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        res = []
        
        def backtrack(idx, comb):
            """

            Args:
                idx (_type_): The current index of the digit being processed in the digits string.
                comb (_type_): The current combination being formed by appending letters.
            """
            
            # When the combination is complete, add it to the results
            if idx == len(digits):
                res.append(comb)
                return
            
            # Iterate over all possible letters for the current digit
            for letter in digit_to_letters[digits[idx]]:
                backtrack(idx + 1, comb + letter)

        backtrack(0, "")
        return res

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
    ]
    
    for i, (digits, expected) in enumerate(test_cases, 1):
        result = solution.letterCombinations(digits)
        # Sort the results for comparison if order doesn't matter
        if sorted(result) != sorted(expected):
            raise AssertionError(f"Test {i} failed: Expected {expected}, got {result}")
        print(f"Test {i} passed.")
