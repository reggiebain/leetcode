# Leetcode 125 - Solution
# Problem - A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a 
# palindrome, or false otherwise.
# Link to post: https://leetcode.com/problems/valid-palindrome/discuss/2704316/Python-or-Faster-than-97-or-Explained

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Lowercase all letters
        s = s.lower()
        # Remove all non alphanumeric characters using ''.join and a filter command on the string
        s = ''.join(filter(lambda x: x.isalnum(), s))
        # Check for palindrome using slicing
        if s[::-1] == s:
            return True
        else:
            return False
