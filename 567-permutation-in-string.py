# Leetcode 567 - Permutation in String - https://leetcode.com/problems/permutation-in-string/
# Prompt: Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise. In other words, return true if 
# one of s1's permutations is the substring of s2.
# Submission/Solution: https://leetcode.com/problems/permutation-in-string/discuss/2711319/Python-or-Sliding-Window-Faster-than-90-or-Explained

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case of s1 size > s2 size since we want s1 contained in s2
        if len(s1) > len(s2):
            return False
        # If s2 contains permutation of s1. Use hash to see anagrams of s1
        s1_dict = {i: s1.count(i) for i in set(s1)} # Generate hash of letter counts in s1
        # Sliding window through s2 of window length s1
        l, r = 0, len(s1) - 1
        window = s2[l:r+1] # Get window of chars in s2
        window_dict = {j: window.count(j) for j in set(window)} # Make hash of window
        if s1_dict == window_dict:
            return True
        while r < len(s2) - 1:
            window_dict[s2[l]] -= 1 # Lower count of letter at left pointer
            if window_dict[s2[l]] == 0:
                del window_dict[s2[l]]
            l, r = l + 1, r + 1 # Slide the window
            if s2[r] not in window_dict:
                window_dict[s2[r]] = window_dict.get(s2[r], 0) + 1
            else:
                window_dict[s2[r]] += 1
            if window_dict == s1_dict:
                return True
        return False 
