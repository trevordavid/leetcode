from typing import List, Dict
from collections import defaultdict

# Given two n-ary trees. Check if they are mirror images of each other or not. You are also given e denoting the number of edges in both trees, and two arrays, A[] and B[]. Each array has 2*e space separated values u,v denoting an edge from u to v for the both trees.

class Solution:
    """
    Check if two n-ary trees are mirror images of each other.
    
    Example:
        Input:
            e = 2
            A[] = {1, 2, 1, 3}
            B[] = {1, 3, 1, 2}
        Output: 1
        
        Tree A:
              1
             / \
            2   3
            
        Tree B:
              1
             / \
            3   2
            
        The trees are mirror images of each other.
        
    Example:
        Input:
            e = 2
            A[] = {1, 2, 1, 3}
            B[] = {1, 2, 1, 3}
        Output: 0
        
        Tree A:
              1
             / \
            2   3
            
        Tree B:
              1
             / \
            2   3
            
        The trees are identical but not mirror images.
    """
    
    def checkMirrorTree(self, e: int, A: List[int], B: List[int]) -> int:
        """
        Check if two n-ary trees are mirror images of each other.
        
        Approach:
        - Construct adjacency lists for both trees
        - For each node in tree A, compare its children with reversed children of the same node in tree B
        - If for every node, the children in tree A match the reversed children in tree B, then the trees are mirror images
        
        Time Complexity: O(n) where n is the number of nodes
                       - We process each edge once while building the trees
                       - Comparing children takes O(n) time in total
        
        Space Complexity: O(n) for storing the adjacency lists
        
        Args:
            e: Number of edges in each tree
            A: Array representing edges of first tree (pairs of u,v)
            B: Array representing edges of second tree (pairs of u,v)
            
        Returns:
            1 if the trees are mirror images, 0 otherwise
        """
        # Build adjacency lists for both trees
        tree_a = defaultdict(list)
        tree_b = defaultdict(list)
        
        # Process edges for tree A
        for i in range(0, 2*e, 2):
            u, v = A[i], A[i+1]
            tree_a[u].append(v)
        
        # Process edges for tree B
        for i in range(0, 2*e, 2):
            u, v = B[i], B[i+1]
            tree_b[u].append(v)
        
        # Check if trees are mirror images
        for node in tree_a:
            # If node doesn't exist in tree B, they're not mirrors
            if node not in tree_b:
                return 0
            
            # Get children from both trees
            children_a = tree_a[node]
            children_b = tree_b[node]
            
            # Check if the length of children is the same
            if len(children_a) != len(children_b):
                return 0
            
            # Check if children of A match reversed children of B
            for i in range(len(children_a)):
                if children_a[i] != children_b[len(children_b) - 1 - i]:
                    return 0
        
        return 1
    
    def checkMirrorTreeStack(self, e: int, A: List[int], B: List[int]) -> int:
        """
        Alternative solution using stacks for comparison.
        
        Approach:
        - Build adjacency lists for both trees
        - For each node, compare children in tree A with popped elements from a stack of children in tree B
        - If they match, the trees are mirror images
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(n) for storing the adjacency lists and stacks
        
        Args:
            e: Number of edges in each tree
            A: Array representing edges of first tree
            B: Array representing edges of second tree
            
        Returns:
            1 if the trees are mirror images, 0 otherwise
        """
        # Build maps for both trees
        tree_a = defaultdict(list)
        tree_b = defaultdict(list)
        
        # Process edges for tree A
        for i in range(0, 2*e, 2):
            u, v = A[i], A[i+1]
            tree_a[u].append(v)
        
        # Process edges for tree B
        for i in range(0, 2*e, 2):
            u, v = B[i], B[i+1]
            tree_b[u].append(v)
        
        # Check if trees are mirror images using stack method
        for node in tree_a:
            if node not in tree_b:
                return 0
                
            # Create a stack of children from tree B
            stack_b = tree_b[node].copy()
            
            # Compare with children from tree A
            for child in tree_a[node]:
                if not stack_b or child != stack_b.pop():
                    return 0
                    
            # If stack_b still has elements, trees are not mirrors
            if stack_b:
                return 0
        
        return 1

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        # e, A[], B[], expected
        (2, [1, 2, 1, 3], [1, 3, 1, 2], 1),               # Example 1: Mirror trees
        (2, [1, 2, 1, 3], [1, 2, 1, 3], 0),               # Example 2: Identical but not mirrors
        (3, [1, 2, 1, 3, 1, 4], [1, 4, 1, 3, 1, 2], 1),   # Three children, mirror image
        (3, [1, 2, 2, 4, 2, 5], [1, 2, 2, 5, 2, 4], 1),   # Mirror with multiple levels
        (4, [1, 2, 1, 3, 2, 4, 3, 5], [1, 3, 1, 2, 3, 5, 2, 4], 1),  # Complex mirror
        (4, [1, 2, 1, 3, 2, 4, 3, 5], [1, 2, 1, 3, 3, 5, 2, 4], 0),  # Not mirror
        (0, [], [], 1),                                    # Empty trees are mirrors
        (1, [1, 2], [1, 3], 0),                           # Different children, not mirrors
    ]
    
    print("Testing main solution:")
    for i, (e, A, B, expected) in enumerate(test_cases, 1):
        result = solution.checkMirrorTree(e, A, B)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Got {result}, Expected {expected}")
    
    print("\nTesting stack-based solution:")
    for i, (e, A, B, expected) in enumerate(test_cases, 1):
        result = solution.checkMirrorTreeStack(e, A, B)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Got {result}, Expected {expected}")