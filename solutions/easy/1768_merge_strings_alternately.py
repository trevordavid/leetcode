from typing import List

class Solution:
    """
    Given two strings word1 and word2, this function merges the strings by adding letters 
    in alternating order, starting with word1. If a string is longer than the other, 
    it appends the additional letters onto the end of the merged string.
    
    Approach:
    - Iterate through both strings simultaneously.
    - Add one character from word1 followed by one character from word2 in each iteration.
    - Continue until we've processed all characters from both strings.
    
    Time Complexity: O(n), where n is the length of the longer string.
    Space Complexity: O(n), for storing the result string.
    """
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = 0

        while i < max(len(word1), len(word2)):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
            i += 1

        return res

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("abc", "pqr", "apbqcr"),             # Same length strings
        ("ab", "pqrs", "apbqrs"),             # First string is shorter
        ("abcd", "pq", "apbqcd"),             # Second string is shorter
        ("", "pqrs", "pqrs"),                 # First string is empty
        ("abcd", "", "abcd"),                 # Second string is empty
        ("a", "p", "ap")                      # Single character strings
    ]
    
    for i, (word1, word2, expected) in enumerate(test_cases, 1):
        result = solution.mergeAlternately(word1, word2)
        assert result == expected, f"Test {i} failed: Expected '{expected}', got '{result}'"
        print(f"Test {i} passed: '{word1}' + '{word2}' -> '{result}'")