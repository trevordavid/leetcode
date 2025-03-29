from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Given the root of a binary tree, return its maximum depth.
    
    A binary tree's maximum depth is the number of nodes along the longest path 
    from the root node down to the farthest leaf node.
    
    Example:
        Input: root = [3,9,20,null,null,15,7]
        Output: 3
        
        The tree has a maximum depth of 3:
             3
            / \
           9  20
              / \
             15  7
    """
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the maximum depth of a binary tree.
        
        Approach:
        - Use a recursive approach to calculate the depth
        - For each node, calculate the maximum depth of its left and right subtrees
        - Return the maximum of those depths plus 1 (for the current node)
        - Base case: If node is None, return 0
        
        Time Complexity: O(n) where n is the number of nodes in the tree
                       - Each node is visited exactly once
        
        Space Complexity: O(h) where h is the height of the tree
                        - In the worst case (skewed tree), this could be O(n)
                        - In the best case (balanced tree), this would be O(log n)
                        - Space is used by the recursion stack
        
        Args:
            root: The root of the binary tree
            
        Returns:
            The maximum depth of the binary tree
        """
        # Base case: empty tree
        if root is None:
            return 0
            
        # Recursively find the depth of left and right subtrees
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        # Return the maximum depth plus 1 (for the current node)
        return max(left_height, right_height) + 1

    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the maximum depth of a binary tree using an iterative approach.
        
        Approach:
        - Use a level-order traversal (BFS) with a queue
        - Keep track of the number of levels we've processed
        
        Time Complexity: O(n) where n is the number of nodes in the tree
        Space Complexity: O(w) where w is the maximum width of the tree
                         - In the worst case, this could be O(n)
                         
        Args:
            root: The root of the binary tree
            
        Returns:
            The maximum depth of the binary tree
        """
        if root is None:
            return 0
            
        # Use a queue for level-order traversal
        queue = [(root, 1)]  # (node, depth)
        max_depth = 0
        
        while queue:
            node, depth = queue.pop(0)
            max_depth = max(max_depth, depth)
            
            if node.left:
                queue.append((node.left, depth + 1))
                
            if node.right:
                queue.append((node.right, depth + 1))
                
        return max_depth

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    # Helper function to construct a binary tree from a list representation
    def create_tree(lst, index=0):
        if index >= len(lst) or lst[index] is None:
            return None
        node = TreeNode(lst[index])
        node.left = create_tree(lst, 2 * index + 1)
        node.right = create_tree(lst, 2 * index + 2)
        return node
    
    # Test cases
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], 3),             # Example tree from the problem
        ([], 0),                                         # Empty tree
        ([1], 1),                                        # Single node
        ([1, 2, 3, 4, 5], 3),                            # Full tree of depth 3
        ([1, None, 2, None, 3, None, 4, None, 5], 5),    # Skewed right tree
        ([1, 2, None, 3, None, 4, None, 5], 5),          # Skewed left tree
        ([1, 2, 3, 4, None, None, 5], 3),                # Irregular tree
    ]
    
    print("Testing recursive solution:")
    for i, (tree_list, expected) in enumerate(test_cases, 1):
        tree = create_tree(tree_list) if tree_list else None
        result = solution.maxDepth(tree)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Got {result}, Expected {expected}")
    
    print("\nTesting iterative solution:")
    for i, (tree_list, expected) in enumerate(test_cases, 1):
        tree = create_tree(tree_list) if tree_list else None
        result = solution.maxDepthIterative(tree)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Got {result}, Expected {expected}")
