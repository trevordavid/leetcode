class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverse the order of words in a string.
        
        Words are separated by one or more spaces. The returned string should have 
        words separated by a single space, with no leading or trailing spaces.
        
        Args:
            s (str): Input string containing words separated by spaces
            
        Returns:
            str: String with words in reverse order
            
        Time Complexity: O(n) where n is the length of the string
        Space Complexity: O(n) to store the split words and reversed string
        """
        #1. Split string to separate into words
        #2. Reverse list of separated words
        #3. Use join method to reinsert spaces
        return " ".join(s.split()[::-1])


def test_solution():
    """Test cases for the Solution class."""
    solution = Solution()
    
    # Test case 1: Regular case
    s1 = "the sky is blue"
    assert solution.reverseWords(s1) == "blue is sky the"
    
    # Test case 2: Multiple spaces between words
    s2 = "  hello world  "
    assert solution.reverseWords(s2) == "world hello"
    
    # Test case 3: Leading and trailing spaces
    s3 = "  Bob    Loves  Alice   "
    assert solution.reverseWords(s3) == "Alice Loves Bob"
    
    # Test case 4: Single word
    s4 = "Alice"
    assert solution.reverseWords(s4) == "Alice"
    
    # Test case 5: Empty string
    s5 = ""
    assert solution.reverseWords(s5) == ""
    
    # Test case 6: Only spaces
    s6 = "     "
    assert solution.reverseWords(s6) == ""
    
    # Test case 7: Single character words
    s7 = "a b c d e"
    assert solution.reverseWords(s7) == "e d c b a"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()