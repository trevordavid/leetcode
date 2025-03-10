from typing import List

class Solution:
    """
    Given two sorted integer arrays, nums1 and nums2, and two integers m and n representing the number of valid elements
    in nums1 and nums2 respectively, merge nums2 into nums1 as one sorted array in non-decreasing order. 

    Note:
    - nums1 has a length of m + n, where the first m elements are the ones to be merged and the last n elements are 0s 
      (placeholders) that should be ignored.
    - The final sorted array is stored in nums1; no value is returned.

    Approach:
    - Make a copy of the first m elements of nums1 to avoid overwriting them.
    - Use two pointers: one for iterating through the copy of nums1 (p1) and one for nums2 (p2).
    - For each position in nums1 (from 0 to m+n-1), compare the elements pointed to by p1 and p2.
      Place the smaller element into nums1 and move the corresponding pointer forward.
    - If one pointer exceeds its array's boundary, simply take elements from the other array.

    Time Complexity: O(m+n) – Each element from both arrays is processed once.
    Space Complexity: O(m) – A copy of the first m elements of nums1 is created.
    """
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Make a copy of the first m elements of nums1.
        nums1_copy = nums1[:m]
        
        # Initialize pointers for nums1_copy and nums2.
        p1 = 0
        p2 = 0
        
        # Merge the two arrays into nums1.
        for p in range(m + n):
            # If nums2 is exhausted or the current element in nums1_copy is less than or equal to nums2[p2]
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1

# -------------------
# Test Cases
# -------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # Each test case is a tuple: (nums1, m, nums2, n, expected merged array)
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
    ]
    
    for i, (nums1, m, nums2, n, expected) in enumerate(test_cases, 1):
        nums1_input = nums1.copy()  # Copy to preserve original test data.
        solution.merge(nums1_input, m, nums2, n)
        assert nums1_input == expected, f"Test {i} failed: Expected {expected}, got {nums1_input}"
        print(f"Test {i} passed.")
