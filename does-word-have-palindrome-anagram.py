# Does a string contain an anagram that is a palindrome?

class Solution:
    def containsPalindrome(self, s: str):
        letter_counts = {c: s.count(c) for c in set(s)} # Create hash of all letter counts in string
        # A palindrome can exist if there's an even number of all letters OR an odd number of 1 letter
        odd_count = 0
        for counts in letter_counts.values(): # Loop over values in library
            if counts % 2 != 0:
                odd_count += 1
            if odd_count > 1:
                return False
        return True   
