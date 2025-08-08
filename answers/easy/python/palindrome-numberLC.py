'''
Breakdown:
    Let's assume the numbers 121 and -121. If we break the problem down into its smallest possible parts we get:

    1. Exclude all negative numbers (the problem says those aren't palindromes)
    2. Compare the first and the last digit.
    
    This works for 2 and 3 digit numbers just fine, because all you have to worry about is the first and last digit.
    But what about larger numbers, like 1221? or 13751? We need to iterate on (repeat) step 2. Let's assume we're going with 1221:
    
    1. Compare digits at position 0 and 3 (the same as step 2 in the previous part)
    2. Compare digits at position 1 and 2 (the iterative step - this proves that we can indeed repeat step 1 infinitely)
    
    Ok, now we can repeat the process...once. what about an absurdly large number like 123456789098765432112345...[etc]? How do we iterate
    over a number that big?
    
    Well if we break down what we are doing even more, we can see that we are comparing the first and last digit (and every subsequent 
    pair of digits following that pattern) form pairs. So if we divide the length by 2, and use that for the limit of our loop,
    we don't need to worry about the 2nd half of the number. If the numbers in the first half match the numbers in the second, 
    we're done anyways.
    
    But that's only true for numbers with an *even* amount of digits. 
    What about odd?
    
    Well if we go back to our first example - we can see that the '2' in '121' is functionally not there. Since the first and last digit (and
    every subsequent digit following that pattern) form a pair, the middle number will never form a pair since there's no second number to
    do that with. So we can safely ignore it, but how do we do that? I mean, assuming we had 121, 
    3 divided by 2 is 1.5, and you can't really index into a 1.5th position, assuming we casted the number to a string.
    
    The answer is in floor division - that is, if we just round down, then 1.5 becomes 1, and that means we only need to check the first number.
    So that means for a number of length 'n':

    numbers to check = n / 2 (rounded down).
    
    And then that's it. Putting it together we have:
    
    1. Exclude all negative numbers.
    2. Compare the first and last digit.
    3. Repeat step 2 comparing first digit + i & last digit + i, until i = range
        - range = n divided by 2 rounded down
        
    Now for the code: 
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        _isPalindrome = True
        s = str(x) 
        first_digit = s[0]
        _range = len(s) // 2 # range = n divided by 2 rounded down
        
        if first_digit == '-':  # step 1: Exclude all negative numbers
            _isPalindrome = False
        else:
            for i in range(_range):
                first_digit = s[i]
                last_digit = s[-(i+1)]
                if first_digit == last_digit: # step 2: compare the first and last digit. repeat until i = range
                    continue
                else:
                    _isPalindrome = False
        
        return _isPalindrome