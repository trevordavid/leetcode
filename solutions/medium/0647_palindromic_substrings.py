from typing import List

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Given a string s, return the number of palindromic substrings in it.
        A string is a palindrome when it reads the same backward as forward.
        A substring is a contiguous sequence of characters within the string.
        """

        def expandAroundCenter(left: int, right: int) -> int:
            """
            Helper function to count palindromic substrings by expanding around the center.
            """
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        n_palindromes = 0
        for center in range(len(s)):
            # Count odd-length palindromes (single character center)
            n_palindromes += expandAroundCenter(center, center)
            # Count even-length palindromes (consecutive character center)
            n_palindromes += expandAroundCenter(center, center + 1)

        return n_palindromes

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("abc", 3),    # 'a', 'b', 'c'
        ("aaa", 6),    # 'a', 'a', 'a', 'aa', 'aa', 'aaa'
        ("racecar", 10), # 'r', 'a', 'c', 'e', 'c', 'a', 'r', 'cec', 'aceca', 'racecar'
        ("", 0),       # Empty string
        ("a", 1)       # Single character
    ]

    solution = Solution()
    for i, (input_str, expected_output) in enumerate(test_cases, 1):
        result = solution.countSubstrings(input_str)
        assert result == expected_output, f"Test case {i} failed: Expected {expected_output}, got {result}"
        print(f"Test case {i} passed: {result}")
