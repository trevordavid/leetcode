"""
    
On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.

Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.

A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.

Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.    

"""

from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        Calculate the exclusive time of each function in a program.
        
        On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.
        Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack.
        
        Args:
            n (int): Number of functions
            logs (List[str]): List of log messages in format "{function_id}:{"start" | "end"}:{timestamp}"
            
        Returns:
            List[int]: Array where the value at the ith index represents the exclusive time for the function with ID i
            
        Approach:
        - Use a stack to track the current function being executed
        - For each log entry:
            - If it's a start log, update the previous function's time and push new function
            - If it's an end log, update the current function's time and pop it from stack
        - Keep track of previous timestamp to calculate time differences
        
        Time Complexity: O(m) where m is the number of logs
        Space Complexity: O(n) for the stack and result array
        """
        ans = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn, typ, time = log.split(":")
            fn, time = int(fn), int(time)

            if typ == 'start':
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(fn)
                prev_time = time
            
            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return ans


def test_solution():
    """Test cases for the Solution class."""
    solution = Solution()
    
    # Test case 1: Simple case with two functions
    n1 = 2
    logs1 = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    expected1 = [3, 4]
    assert solution.exclusiveTime(n1, logs1) == expected1
    
    # Test case 2: Single function
    n2 = 1
    logs2 = ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]
    expected2 = [8]
    assert solution.exclusiveTime(n2, logs2) == expected2
    
    # Test case 3: Multiple functions with recursive calls
    n3 = 3
    logs3 = ["0:start:0", "0:start:2", "1:start:3", "1:end:3", "2:start:4", "2:end:4", "0:end:5"]
    expected3 = [4, 1, 1]
    assert solution.exclusiveTime(n3, logs3) == expected3
    
    # Test case 4: Functions with no overlap
    n4 = 2
    logs4 = ["0:start:0", "0:end:2", "1:start:3", "1:end:5"]
    expected4 = [3, 3]
    assert solution.exclusiveTime(n4, logs4) == expected4
    
    # Test case 5: Functions with immediate end
    n5 = 2
    logs5 = ["0:start:0", "0:end:0", "1:start:1", "1:end:1"]
    expected5 = [1, 1]
    assert solution.exclusiveTime(n5, logs5) == expected5
    
    # Test case 6: Complex nested functions
    n6 = 3
    logs6 = ["0:start:0", "1:start:1", "2:start:2", "2:end:3", "1:end:4", "0:end:5"]
    expected6 = [2, 2, 2]
    assert solution.exclusiveTime(n6, logs6) == expected6
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()