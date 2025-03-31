from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Find the minimum depth of a binary tree.
        
        The minimum depth is the number of nodes along the shortest path 
        from the root node down to the nearest leaf node.
        
        Args:
            root (Optional[TreeNode]): Root node of the binary tree
            
        Returns:
            int: Minimum depth of the tree. Returns 0 for empty tree.
            
        Time Complexity: O(n) where n is the number of nodes in the tree
        Space Complexity: O(w) where w is the maximum width of the tree
        """
        if not root:
            return 0  # If the tree is empty, return depth 0
        
        queue = deque([(root, 1)])  # Initialize the queue with the root node and depth 1
        
        while queue:
            node, depth = queue.popleft()
            
            # If it's a leaf node, return the current depth
            if not node.left and not node.right:
                return depth
            
            # Add left and right children to the queue, if they exist
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))


def test_solution():
    """Test cases for the Solution class."""
    solution = Solution()
    
    # Test case 1: Simple tree
    #     3
    #    / \
    #   9   20
    #       / \
    #      15  7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    assert solution.minDepth(root1) == 2  # Path: 3 -> 9
    
    # Test case 2: Single node
    root2 = TreeNode(1)
    assert solution.minDepth(root2) == 1
    
    # Test case 3: Empty tree
    assert solution.minDepth(None) == 0
    
    # Test case 4: Perfect binary tree
    #     1
    #    / \
    #   2   3
    #  / \ / \
    # 4  5 6  7
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.left.left = TreeNode(4)
    root3.left.right = TreeNode(5)
    root3.right.left = TreeNode(6)
    root3.right.right = TreeNode(7)
    
    assert solution.minDepth(root3) == 3  # Path: 1 -> 2 -> 4
    
    # Test case 5: Skewed tree
    #     1
    #      \
    #       2
    #        \
    #         3
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.right = TreeNode(3)
    
    assert solution.minDepth(root4) == 3  # Path: 1 -> 2 -> 3
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()