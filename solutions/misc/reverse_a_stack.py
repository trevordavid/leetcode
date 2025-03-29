from typing import List

class Solution:
    """
    This class provides methods to reverse a stack.
    
    A stack follows the Last-In-First-Out (LIFO) principle, and reversing it
    means the first inserted element becomes the top element.
    
    Example:
    Input stack: [1, 2, 3, 4] (top is 4)
    Reversed stack: [4, 3, 2, 1] (top is 1)
    
    Two approaches are implemented:
    1. Recursive approach - using the call stack for auxiliary storage
    2. Iterative approach - using an auxiliary stack
    """
    
    def reverse_stack_recursive(self, stack: List[int]) -> None:
        """
        Reverses a stack in-place using recursion.
        
        Approach:
        - Use recursion to reach the bottom of the stack
        - For each element popped, insert it at the bottom of the reversed stack
        
        Time Complexity: O(n²) due to insert_at_bottom operation for each element
        Space Complexity: O(n) for the recursive call stack
        
        Args:
            stack (List[int]): The stack to be reversed (modified in-place)
        
        Returns:
            None: The stack is modified in-place
        """
        if len(stack) == 0:
            return
            
        # Remove the top element
        top = stack.pop()
        
        # Recursively reverse the remaining stack
        self.reverse_stack_recursive(stack)
        
        # Insert the top element at the bottom of the reversed stack
        self._insert_at_bottom(stack, top)
    
    def _insert_at_bottom(self, stack: List[int], item: int) -> None:
        """
        Helper method to insert an element at the bottom of a stack.
        
        Args:
            stack (List[int]): The stack where the item will be inserted
            item (int): The item to insert at the bottom
            
        Returns:
            None: The stack is modified in-place
        """
        if len(stack) == 0:
            stack.append(item)
            return
            
        # Remove the top element
        top = stack.pop()
        
        # Recursively insert at the bottom
        self._insert_at_bottom(stack, item)
        
        # Push the top element back
        stack.append(top)
    
    def reverse_stack_iterative(self, stack: List[int]) -> List[int]:
        """
        Reverses a stack using an auxiliary stack.
        
        Approach:
        - Create an auxiliary stack
        - Pop elements from the original stack and push them onto the auxiliary stack
        - Pop elements from the auxiliary stack and push them back to the original stack
        
        Time Complexity: O(n) where n is the number of elements in the stack
        Space Complexity: O(n) for the auxiliary stack
        
        Args:
            stack (List[int]): The stack to be reversed
            
        Returns:
            List[int]: The reversed stack
        """
        if not stack:
            return stack
            
        # Create an auxiliary stack
        aux_stack = []
        
        # Pop elements from original stack and push to auxiliary stack
        # This reverses the order
        while stack:
            aux_stack.append(stack.pop())
        
        # The auxiliary stack now contains elements in reversed order
        # Return the auxiliary stack as the reversed stack
        return aux_stack

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        [1, 2, 3, 4, 5],       # Normal case with odd number of elements
        [10, 20, 30, 40],       # Normal case with even number of elements
        [42],                   # Stack with single element
        [],                     # Empty stack
        [5, 5, 5, 5, 5],        # Stack with duplicate elements
    ]
    
    print("Testing recursive stack reversal:")
    for i, stack in enumerate(test_cases, 1):
        original = stack.copy()  # Save a copy for display
        expected = original.copy()
        expected.reverse()      # Built-in reverse for comparison
        
        # Apply recursive reversal
        stack_copy = original.copy()
        solution.reverse_stack_recursive(stack_copy)
        
        success = stack_copy == expected
        print(f"Test {i}: {'✓' if success else '✗'}")
        if not success:
            print(f"  Original: {original}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {stack_copy}")
    
    print("\nTesting iterative stack reversal:")
    for i, stack in enumerate(test_cases, 1):
        original = stack.copy()  # Save a copy for display
        expected = original.copy()
        expected.reverse()      # Built-in reverse for comparison
        
        # Apply iterative reversal
        stack_copy = original.copy()
        reversed_stack = solution.reverse_stack_iterative(stack_copy)
        
        success = reversed_stack == expected
        print(f"Test {i}: {'✓' if success else '✗'}")
        if not success:
            print(f"  Original: {original}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {reversed_stack}")
            