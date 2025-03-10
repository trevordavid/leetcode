from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    """
    Given the head of a singly linked list, this function returns the middle node.
    If there are two middle nodes, it returns the second middle node.
    
    Approach:
    - Utilize two pointers: 'slow' and 'fast'.
    - 'slow' advances one node at a time.
    - 'fast' advances two nodes at a time.
    - When 'fast' reaches the end of the list, 'slow' will be at the middle node.
    
    Time Complexity: O(n), where n is the number of nodes in the linked list.
    Space Complexity: O(1), as no additional space is used that scales with input size.
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Traverse the list with two pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 'slow' is now pointing to the middle node
        return slow

# -------------------
# Test Cases
# -------------------
def list_to_linkedlist(elements):
    """Helper function to convert a list to a linked list."""
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

def linkedlist_to_list(node):
    """Helper function to convert a linked list back to a regular list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5]),  # Odd number of nodes
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]),  # Even number of nodes
        ([1], [1]),  # Single node
        ([1, 2], [2]),  # Two nodes
        ([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7])  # Larger list
    ]
    
    for i, (input_list, expected_output) in enumerate(test_cases, 1):
        head = list_to_linkedlist(input_list)
        middle_node = solution.middleNode(head)
        result = linkedlist_to_list(middle_node)
        assert result == expected_output, f"Test case {i} failed: Expected {expected_output}, got {result}"
        print(f"Test case {i} passed: {result}")
