
'''

Tag: Easy Math

Ultimate Goal: Could you solve it without converting the integer to a string?

-------------------------------------------------------------------------------------------

Def: A palindromic number (or numeral palindrome) is a number that remains the same when its digits are reversed, like 121 or 132231. 

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

'''

def run(x):

    if x < 0:
        print(False)
    else: 
        x_str = str(x)

        x_rev = x_str[::-1]

        y = int(x_rev)

        print(x == y)
