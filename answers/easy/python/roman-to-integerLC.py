import pdb

class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        
        ^^^ map each letter to a number, then just add based on position since it's a string
        steps:
        convert 1 char to 1 integer using a map
        convert string of size 2 to integer using a map (including addition)
        convert string of size n to integer using map (inaccurate addition allowed)
        convert string of size n to integer using map (ensure accurate addition)
        '''

        roman_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        num = 0
        
       #d pdb.set_trace()
        for i in range(len(s) - 1):
            if s[i] not in roman_dict:
                print("ERR: INVALID ROMAN NUMERAL")
                break
            else:
                if roman_dict[s[i]] < roman_dict[s[(i + 1)]]:
                    num = num - roman_dict[s[i]]
                    print(f"{num}")
                else:
                    num = num + roman_dict[s[i]]
                    print(f"{num}")
                
        num = num + roman_dict[s[-1]]    
            
        return num
    
    print(f"{romanToInt(romanToInt, "MCMXCIV")}")