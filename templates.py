class Templates:
    """
    A collection of common algorithm patterns used in LeetCode problems.
    Each method implements a standard algorithm pattern with documentation
    and examples of usage.
    """
    
    def __init__(self):
        """Initialize the Templates class."""
        pass
    
    # Binary Search
    def binary_search(self, nums, target):
        """
        Standard binary search implementation.
        
        Args:
            nums: A sorted list of integers
            target: The value to search for
            
        Returns:
            The index of the target if found, -1 otherwise
            
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Avoid potential integer overflow with (left + right) // 2
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
    
    # DFS for Tree Traversal
    def dfs_tree(self, root):
        """
        Depth-first search traversal of a binary tree.
        
        Args:
            root: The root node of a binary tree
            
        Returns:
            A list containing the values of the tree in pre-order traversal
            
        Time Complexity: O(n)
        Space Complexity: O(h) where h is the height of the tree
        """
        result = []
        
        def dfs(node):
            if not node:
                return
            
            # Pre-order traversal (root, left, right)
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return result
    
    # Iterative DFS (to avoid recursion stack overhead)
    def dfs_tree_iterative(self, root):
        """
        Iterative depth-first search traversal of a binary tree.
        
        Args:
            root: The root node of a binary tree
            
        Returns:
            A list containing the values of the tree in pre-order traversal
            
        Time Complexity: O(n)
        Space Complexity: O(h) where h is the height of the tree
        """
        if not root:
            return []
            
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            # Push right first so left is processed first (LIFO)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return result
    
    # BFS for Tree Traversal
    def bfs_tree(self, root):
        """
        Breadth-first search traversal of a binary tree.
        
        Args:
            root: The root node of a binary tree
            
        Returns:
            A list containing the values of the tree in level-order traversal
            
        Time Complexity: O(n)
        Space Complexity: O(w) where w is the max width of the tree
        """
        if not root:
            return []
        
        result = []
        # Using collections.deque for O(1) popleft operation
        from collections import deque
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return result
    
    # Backtracking Template
    def backtracking(self, input_data):
        """
        Generic backtracking template.
        
        Args:
            input_data: The data to process
            
        Returns:
            A list containing all valid solutions
            
        Example:
            For a subset generation problem
        """
        results = []
        
        def backtrack(start, current_path):
            # Add the current path to results
            results.append(current_path[:])
            
            # Explore candidates
            for i in range(start, len(input_data)):
                # Add candidate to path
                current_path.append(input_data[i])
                
                # Recursive call with updated state
                backtrack(i + 1, current_path)
                
                # Backtrack (remove the last added element)
                current_path.pop()
        
        backtrack(0, [])
        return results
    
    # Two Pointers - Basic
    def two_pointers(self, nums, target):
        """
        Two-pointer technique for finding a pair that sums to target in a sorted array.
        
        Args:
            nums: A sorted list of integers
            target: The target sum
            
        Returns:
            Indices of the two numbers that add up to target, or [-1, -1] if not found
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
        return [-1, -1]
    
    # Sliding Window - Fixed Size
    def sliding_window_fixed(self, nums, k):
        """
        Fixed-size sliding window to find maximum sum subarray of size k.
        
        Args:
            nums: A list of integers
            k: The size of the window
            
        Returns:
            Maximum sum of any subarray of size k
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums or k <= 0 or k > len(nums):
            return 0
            
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for i in range(k, len(nums)):
            # Add new element and remove first element of previous window
            window_sum = window_sum + nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
            
        return max_sum
    
    # Sliding Window - Variable Size
    def sliding_window_variable(self, nums, target):
        """
        Variable-size sliding window to find minimum length subarray with sum >= target.
        
        Args:
            nums: A list of positive integers
            target: The target sum
            
        Returns:
            Minimum length of a subarray with sum >= target, or 0 if impossible
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0
            
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink window from left while condition is satisfied
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
                
        return min_length if min_length != float('inf') else 0
    
    # Topological Sort
    def topological_sort(self, num_vertices, edges):
        """
        Topological sorting for Directed Acyclic Graph (DAG).
        
        Args:
            num_vertices: Number of vertices in the graph
            edges: List of directed edges as [from, to] pairs
            
        Returns:
            Topologically sorted list of vertices, or empty list if cycle exists
            
        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        """
        # Build adjacency list
        graph = [[] for _ in range(num_vertices)]
        in_degree = [0] * num_vertices
        
        for src, dst in edges:
            graph[src].append(dst)
            in_degree[dst] += 1
        
        # Queue for vertices with no incoming edges
        from collections import deque
        queue = deque([v for v in range(num_vertices) if in_degree[v] == 0])
        
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in graph[vertex]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If topological sort is possible, result will contain all vertices
        return result if len(result) == num_vertices else []
    
    # Union Find (Disjoint Set)
    def union_find(self, n):
        """
        Union-Find data structure implementation with path compression and union by rank.
        
        Args:
            n: Number of elements
            
        Returns:
            Three functions: find, union, and connected
            
        Time Complexity:
            - Find: O(α(n)) - amortized nearly O(1)
            - Union: O(α(n))
            - Connected: O(α(n))
        Space Complexity: O(n)
        """
        # Initialize parent and rank arrays
        parent = list(range(n))
        rank = [0] * n
        
        # Find operation with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        # Union operation with union by rank
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return False
            
            # Attach smaller rank tree under root of higher rank tree
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                # If ranks are same, make one as root and increment its rank
                parent[root_y] = root_x
                rank[root_x] += 1
            
            return True
        
        # Check if two elements are in the same set
        def connected(x, y):
            return find(x) == find(y)
        
        return find, union, connected
    
    # Dynamic Programming - 0/1 Knapsack
    def knapsack(self, weights, values, capacity):
        """
        0/1 Knapsack problem using dynamic programming.
        
        Args:
            weights: List of weights of items
            values: List of values of items
            capacity: Maximum capacity of knapsack
            
        Returns:
            Maximum value that can be obtained
            
        Time Complexity: O(n * capacity)
        Space Complexity: O(capacity) - optimized from O(n * capacity)
        """
        n = len(weights)
        
        # Optimize space complexity by using 1D array
        dp = [0] * (capacity + 1)
        
        for i in range(n):
            # Process in reverse to avoid using items multiple times
            for w in range(capacity, weights[i] - 1, -1):
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
                
        return dp[capacity]
    
    # Dijkstra's Algorithm
    def dijkstra(self, graph, start):
        """
        Dijkstra's algorithm for single-source shortest paths.
        
        Args:
            graph: Adjacency list with weights as (neighbor, weight) tuples
            start: Starting vertex
            
        Returns:
            Dictionary mapping each vertex to its shortest distance from start
            
        Time Complexity: O((V + E) log V) with binary heap
        Space Complexity: O(V)
        """
        import heapq
        
        # Initialize distances with infinity
        distances = {vertex: float('infinity') for vertex in range(len(graph))}
        distances[start] = 0
        
        # Priority queue for vertices to visit
        pq = [(0, start)]
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            # Skip if we've found a better path already
            if current_distance > distances[current_vertex]:
                continue
                
            # Check all neighbors
            for neighbor, weight in graph[current_vertex]:
                distance = current_distance + weight
                
                # If we've found a better path
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
                    
        return distances