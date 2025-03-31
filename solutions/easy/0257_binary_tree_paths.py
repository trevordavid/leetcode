from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Find all root-to-leaf paths in a binary tree.
        
        Args:
            root (Optional[TreeNode]): Root node of the binary tree
            
        Returns:
            List[str]: List of all root-to-leaf paths in the format "root->node1->node2->...->leaf"
            
        Time Complexity: O(n) where n is the number of nodes in the tree
        Space Complexity: O(h) where h is the height of the tree (recursion stack)
        """
        def dfs(node: Optional[TreeNode], path: List[str], result: List[str]) -> None:
            """
            Depth-first search to find all root-to-leaf paths.
            
            Args:
                node (Optional[TreeNode]): Current node
                path (List[str]): Current path from root to current node
                result (List[str]): List to store all found paths
            """
            if not node:
                return
                
            path.append(str(node.val))
            
            if not node.left and not node.right:
                result.append('->'.join(path))
            else:
                dfs(node.left, path, result)
                dfs(node.right, path, result)
                
            path.pop()  # Backtrack by removing last element

        result = []
        dfs(root, [], result)
        return result


def test_solution():
    """Test cases for the Solution class."""
    solution = Solution()
    
    # Test case 1: Simple tree
    #     1
    #    / \
    #   2   3
    #    \
    #     5
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    
    expected1 = ["1->2->5", "1->3"]
    assert solution.binaryTreePaths(root1) == expected1
    
    # Test case 2: Single node
    root2 = TreeNode(1)
    expected2 = ["1"]
    assert solution.binaryTreePaths(root2) == expected2
    
    # Test case 3: Empty tree
    assert solution.binaryTreePaths(None) == []
    
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
    
    expected3 = ["1->2->4", "1->2->5", "1->3->6", "1->3->7"]
    assert solution.binaryTreePaths(root3) == expected3
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()