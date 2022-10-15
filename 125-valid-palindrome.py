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
