# Leetcode 209 - Minimum Size Subarray
# Problem Link: https://leetcode.com/problems/minimum-size-subarray-sum/
# Solution Link: https://leetcode.com/problems/minimum-size-subarray-sum/discuss/2761638/Python-or-O(n)-Solution-or-Commented-or-Sliding-Window

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        output = len(nums) + 1 # Set output to lengths of nums + 1 (invalid result)
        l, total = 0, 0 # Set left pointer and total of sum
        for r in range(len(nums)): # Loop over all elements O(n) to begin summing
            total += nums[r] # Add to total
            while total >= target: # If sum is >= target then we need to see if we can make it smaller
                output = min(output, r - l + 1) # Set output to r+l-1 (width of sliding window)
                total -= nums[l] # Try to make window as small as we can. First subtract what's at l
                l += 1 # Then increment l forwards
        return 0 if output == len(nums) + 1 else output    
