'''
Breakdown:

    Ok, so this one was a bit of a doozy for me. The most difficult part was figuring out *how* exactly we do what we're doing,
    rather than *what* to do. The reason why will become clear in a moment. 
    
    Roman numerals are made up of these symbols: 
    
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
    
    The natural way to store these pairs is with a dictionary (or map), so each 
    Roman numeral points to its integer value.
    
    Ok, so now we know what data structure we are going to use. 
    Next, in keeping with our "Problem-solving First" mantra, let's break down the problem into its smallest possible parts:
    
    1. Convert one Roman numeral to its integer equivalent // proves that we can handle a single case
    2. Extend step 1 to repeating values (e.g, II = 2, III = 3) //proves that we can repeat the single case
     
    But, we're only halfway done.  Like I said earlier, it's not *what* we are doing that's tricky - it's *how*. 
    So let's try to work on the logic in more detail, and in the process I'll show you where I got stumped.
    
    Right now, what we need to do is express the rule that governs subtraction:
    
    1. Loop through all the characters
    2. Convert each character to its integer equivalent
    3. If the current number is less than the next number, subtract from the total, else add it
            
    But...try to code and run this as is....and it crashes. Why? Well currently, the program stops 
    before I ever get to add or subtract. The issue is contained in step 3. What we're actually doing in step 3 is saying:
    
    if current < next:
        subtract from total
    else:
        add to total
        
    The problem with this is that if I get to the end of the string, there's no "next" to compare to, so we're indexing
    out of bounds.
    
    This stumped me for a while. I eventually realized that I could simply handle the last character on its own, 
    since you will always have to add the last character (there's no "next" to compare it to anyway):
    
    1. Loop through all the characters *except* the last character // *The fix!!*
    2. Convert each character to its integer equivalent
    3. If the current number is less than the next number, subtract from the total, else add it
    4. Add the last character // *The fix!!*
    
    And now for the code:
'''
class Solution:
    def romanToInt(self, s: str) -> int:

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
        
        for i in range(len(s) - 1):
            if s[i] not in roman_dict:
                print("ERR: INVALID ROMAN NUMERAL")
                break
            else:
                if roman_dict[s[i]] < roman_dict[s[(i + 1)]]:
                    num = num - roman_dict[s[i]]
                else:
                    num = num + roman_dict[s[i]]
                
        num = num + roman_dict[s[-1]]    
            
        return num
    