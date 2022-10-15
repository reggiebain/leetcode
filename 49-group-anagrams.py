# Leetcode 49 - Group Anagrams
# Q: Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Anagrams call for hash/dictionary. Create a dict where the keys are sets.
# Make each hash an alphabetized key and then the actual word/letters as the value
# NOTE: dictionary.get(keyname, value); keyname is key you want value from, value to return if key dne.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_dict = {}
        for s in strs:
            alph = ''.join(sorted(s)) # Alphabetize string
            if alph not in s_dict: # If key not in hash
                s_dict[alph] = s_dict.get(alph, [s]) # Add key and set value to s in list
            else:
                s_dict[alph].append(s) # If alphabetized key is already in list, simply append s to list
        return s_dict.values() # Return values of dictionary since order of return doesn't matter
