# Leetcode 258 - Digit Sum
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Explanation: 
# Undoubtedly, many others have written about a similar path to solving it. They are all based in the modular arithmetic described 
# in this article https://en.wikipedia.org/wiki/Digital_root. One can show that:
# n = 1,234 = 1x10<sup>3</sup> + 2x10<sup>2</sup> + 3x10<sup>1</sup> + 4x10<sup>0</sup>
# n = (1+999)x10<sup>2</sup> + (1+99)x10<sup>1</sup> + (1+9)x10<sup>0</sup>
# n = (999x10<sup>2</sup> + 99x10<sup>1</sup> + 9x10<sup>0</sup>) + (1+2+3+4)
# n = (number divisible by 9) + (sum of digits of n)
# n (mod 9) = (number divisible by 9) (mod 9) + (sum of digits of n) (mod 9)
# Thus --> n (mod 9) = (sum of digits of n) (mod 9) 

# This means that any number mod 9 equals the sum of its digits mod 9. So to get the sum of the digits we use...
# 1. Digit Sum = n (mod 9) + 9

# But what about when n divisible by 9? Arithmetic tells us that any number whose digits add to 9, must be divisible by 9 thus we add a second condition.

# 2. Digit Sum = 9 when n (mod 9) = 0

# Finally, the edge case (which Leetcode tests) of n = 0, where obviously the sum of the digits is 0.

# 3. Digit Sum = 0 when n = 0

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return (num % 9)
