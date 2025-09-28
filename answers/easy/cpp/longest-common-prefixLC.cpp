#include <string>
#include <iostream>
#include <vector>
using namespace std;

/*
This problem was one of the first that I had tackled for a while, so I had a little trouble
at first.

First order of business: break the problem down, as always:
1. compare one character of two of the strings
2. compare one character across all of the strings
3. compare two characters across all of the strings
4. compare one character across two strings, one of length n and another of length n - 1
5. return prefix

These steps cover almost all the cases that arise from the two given examples on LeetCode:
[flower, flow, flight]
[dog, racecar, car]

Some strings will be longer than others, so step 4 covers that. In all
other cases where there is a value, the logic holds soundly. The tricky part, though, is in the edge cases.

Something you need to be aware of at all times is whether you've actually thought of everything when
solving a problem. For example:
- What if I gave you the input []?
- Or what about ["a"]?

Either one breaks the (admittedly naive) logic. Why? Well we didn't actually check whether or not the vector was empty, 
or what happens when there's only one string. Keep in mind that the function gives us the vector by reference,
not by value, and the question never guaranteed a specific vector size - but you 
might infer that from the wording or the examples. You could easily try to index into something that just isn't there.

So, revising the plan:

1. compare one character of two of the strings
2. compare one character across all of the strings
3. compare two characters across all of the strings
4. compare one character across two strings, one of length n and another of length n - 1
5. check for null cases (or empty in the case of vectors)
6. check for edge cases (strs.size() == 1)
7. return prefix

And if we compress this into actual working logic:

1. handle trivial inputs (steps 5 and 6 from before)
2. check each character until there is a mismatch (steps 1-4)
3. return prefix

Last but not least, here's the code:
*/

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string lcf = "";
        bool done = false;

        if (strs.empty())
        {
            return "";
        }

        if (strs.size() == 1)
        {
            return strs[0];
        }

        for (size_t curr_char = 0; curr_char < strs[0].size() && !done; ++curr_char) 
        {
            char c = strs[0][curr_char];
            for (size_t i = 1; i < strs.size(); ++i)
            {
                if (curr_char >= strs[i].size() || strs[i][curr_char] != c)
                {
                    done = true;
                    break;
                }
            }

            if (!done)
            {
                lcf += c;
            }
        }

        return lcf;
    }
};
