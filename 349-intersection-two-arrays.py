# Leetcode 349: https://leetcode.com/problems/intersection-of-two-arrays/
# Post: https://leetcode.com/problems/intersection-of-two-arrays/discuss/2737320/Python-or-Sets-or-Faster-than-98-or-Explained!

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Pick the shorter of the two sets
        set1, set2 = set(nums1), set(nums2)
        intersect = []
        if len(set1) < len(set2):
            small, large = set1, set2
        else:
            small, large = set2, set1
        for i in small:
            if i in large:
                intersect.append(i)
        return list(set(intersect)) 
