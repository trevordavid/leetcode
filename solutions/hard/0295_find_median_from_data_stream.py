import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize two heaps:
        - self.low: Max-heap (simulated using negative values) to store the smaller half of the numbers.
        - self.high: Min-heap to store the larger half of the numbers.
        """
        self.low = []  # Max-heap (inverted to use Python's min-heap)
        self.high = []  # Min-heap

    def addNum(self, num: int) -> None:
        """
        Add a number into the data structure.
        """
        # Add to max-heap (invert num to simulate max-heap)
        heapq.heappush(self.low, -num)
        # Balance the heaps by moving the largest of low to high
        heapq.heappush(self.high, -heapq.heappop(self.low))

        # Ensure low has at least as many elements as high
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        """
        Return the median of all elements so far.
        """
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (-self.low[0] + self.high[0]) / 2.0

# Test cases to validate the implementation
if __name__ == "__main__":
    # Test Case 1
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5, "Test Case 1 Failed"
    mf.addNum(3)
    assert mf.findMedian() == 2.0, "Test Case 1 Failed"

    # Test Case 2
    mf = MedianFinder()
    mf.addNum(5)
    mf.addNum(15)
    mf.addNum(10)
    assert mf.findMedian() == 10.0, "Test Case 2 Failed"

    # Test Case 3
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    mf.addNum(3)
    mf.addNum(4)
    assert mf.findMedian() == 2.5, "Test Case 3 Failed"

    print("All test cases passed.")
