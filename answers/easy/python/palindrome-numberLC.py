class Solution:
    def isPalindrome(self, x: int) -> bool:
        _isPalindrome = True
        s = str(x)
        first_digit = s[0]
        _range = len(s) // 2
        
        if first_digit == '-':
            _isPalindrome = False
        else:
            for i in range(_range):
                first_digit = s[i]
                last_digit = s[-(i+1)]
                if first_digit == last_digit:
                    continue
                else:
                    _isPalindrome = False
        
        return _isPalindrome