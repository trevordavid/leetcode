from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of val from nums in-place.
        
        The order of the elements may be changed. The first k elements of nums 
        should contain the elements which are not equal to val. The remaining 
        elements of nums are not important as well as the size of nums.
        
        Args:
            nums (List[int]): Input array to modify in-place
            val (int): Value to remove from the array
            
        Returns:
            int: Number of elements in nums which are not equal to val
            
        Time Complexity: O(n) where n is the length of nums
        Space Complexity: O(1) as we modify the array in-place
        """
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i


def test_solution():
    """Test cases for the Solution class."""
    solution = Solution()
    
    # Test case 1: Regular case with multiple occurrences
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    assert k1 == 2
    assert nums1[:k1] == [2, 2]
    
    # Test case 2: No occurrences of val
    nums2 = [0, 1, 2, 3, 4]
    val2 = 5
    k2 = solution.removeElement(nums2, val2)
    assert k2 == 5
    assert nums2[:k2] == [0, 1, 2, 3, 4]
    
    # Test case 3: All elements are val
    nums3 = [2, 2, 2, 2]
    val3 = 2
    k3 = solution.removeElement(nums3, val3)
    assert k3 == 0
    
    # Test case 4: Empty array
    nums4 = []
    val4 = 1
    k4 = solution.removeElement(nums4, val4)
    assert k4 == 0
    
    # Test case 5: Single element array
    nums5 = [1]
    val5 = 1
    k5 = solution.removeElement(nums5, val5)
    assert k5 == 0
    
    # Test case 6: Single element array, different val
    nums6 = [1]
    val6 = 2
    k6 = solution.removeElement(nums6, val6)
    assert k6 == 1
    assert nums6[:k6] == [1]
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()