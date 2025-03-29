from typing import Optional

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Given the root of a binary tree, check whether it is a mirror of itself 
    (i.e., symmetric around its center).
    
    Example:
        Input: root = [1,2,2,3,4,4,3]
        Output: true
        
        The tree is symmetric:
             1
            / \
           2   2
          / \ / \
         3  4 4  3
         
    Example:
        Input: root = [1,2,2,null,3,null,3]
        Output: false
        
        The tree is not symmetric:
             1
            / \
           2   2
            \   \
            3    3
    """
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is symmetric around its center.
        
        Approach:
        - Use a recursive helper function to check if two subtrees are mirrors of each other
        - Initially, we compare the left and right subtrees of the root
        - Two subtrees are mirrors if:
          1. Their root values are the same
          2. Left's left subtree is a mirror of right's right subtree
          3. Left's right subtree is a mirror of right's left subtree
        
        Time Complexity: O(n) where n is the number of nodes in the tree
                       - Each node is visited exactly once
        
        Space Complexity: O(h) where h is the height of the tree
                        - In the worst case (skewed tree), space complexity is O(n)
                        - In the best case (balanced tree), space complexity is O(log n)
                        - Space is used by the recursion stack
        
        Args:
            root: The root of the binary tree
            
        Returns:
            True if the tree is symmetric, False otherwise
        """
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)
        
    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        """
        Helper function to check if two subtrees are mirrors of each other.
        
        Args:
            left: Root of the left subtree
            right: Root of the right subtree
            
        Returns:
            True if the subtrees are mirrors, False otherwise
        """
        # If both nodes are None, they are mirrors
        if left is None and right is None:
            return True
            
        # If only one is None, they are not mirrors
        if left is None or right is None:
            return False
            
        # Check if values are the same and subtrees are mirrors
        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPair = self.isMirror(left.right, right.left)
            return outPair and inPair
        else:
            return False
    
    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is symmetric using an iterative approach.
        
        Approach:
        - Use a queue to perform a level-order traversal
        - For each pair of nodes we need to compare, add them to the queue
        - Process pairs from the queue and check if they match
        - For each pair, add their children to the queue in correct order for comparison
        
        Time Complexity: O(n) where n is the number of nodes in the tree
                       - Each node is processed exactly once
        
        Space Complexity: O(w) where w is the maximum width of the tree
                        - In the worst case, this could be O(n)
        
        Args:
            root: The root of the binary tree
            
        Returns:
            True if the tree is symmetric, False otherwise
        """
        if root is None:
            return True
            
        # Use a queue to store pairs of nodes to compare
        queue = [(root.left, root.right)]
        
        while queue:
            left, right = queue.pop(0)
            
            # If both nodes are None, continue to next pair
            if left is None and right is None:
                continue
                
            # If only one is None or values don't match, tree is not symmetric
            if left is None or right is None or left.val != right.val:
                return False
                
            # Add the pairs that need to be compared
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
            
        return True

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
        ([1, 2, 2, 3, 4, 4, 3], True),                    # Example 1: symmetric tree
        ([1, 2, 2, None, 3, None, 3], False),             # Example 2: non-symmetric tree
        ([], True),                                        # Empty tree is symmetric
        ([1], True),                                       # Single node is symmetric
        ([1, 2, 3], False),                                # Different values at same level
        ([1, 2, 2, 2, None, None, 2], True),              # Symmetric with depth 3
        ([1, 2, 2, None, 3, 3, None], True),              # Another symmetric example
        ([1, 2, 2, None, 3, 4, None], False),             # Different values in subtrees
    ]
    
    print("Testing recursive solution:")
    for i, (tree_list, expected) in enumerate(test_cases, 1):
        tree = create_tree(tree_list) if tree_list else None
        result = solution.isSymmetric(tree)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Got {result}, Expected {expected}")
    
    print("\nTesting iterative solution:")
    for i, (tree_list, expected) in enumerate(test_cases, 1):
        tree = create_tree(tree_list) if tree_list else None
        result = solution.isSymmetricIterative(tree)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Got {result}, Expected {expected}")
        
