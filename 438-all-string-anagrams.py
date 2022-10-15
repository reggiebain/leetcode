# Leetcode 438 - Find all anagrams of a string
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# My solution on Leetcode: https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/2555598/Python-Easy-Sliding-Window-Approach-O(n) 
# Key: Uses sliding window approach and hash map (python dictionary)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Edge cases
        if len(s) < len(p):
            return []
        # Create sliding window hash map to check for anagram
        l, r = 0, len(p) - 1 # Declare 2 pointers at 0 and p characters later
        p_dict = {c: p.count(c) for c in set(p)} # Create hash of counts of each letter in p.
        window = s[l:r+1] # Set initial window of characters from s
        s_dict = {c: window.count(c) for c in set(window)} # Create initial window hash
        output = []
        if p_dict == s_dict:
            output.append(0) # Initial check pre loop
        while r <= len(s) - 2: # While r goes up to len(s) - 2 since we always increment in loop
            s_dict[s[l]] -= 1 # Decrement counter for character at l
            if s_dict[s[l]] == 0: # If that counter is 0, del hash ke
                del s_dict[s[l]]
            l, r = l + 1, r + 1 # Increment counters to move window
            s_dict[s[r]] = s_dict.get(s[r],0) + 1 # Add new entry to hash at location r, +1, 0 if not there
            if p_dict == s_dict: # Check if hash of p and of window are equal
                output.append(l) # If so, increment counter
        return output  
