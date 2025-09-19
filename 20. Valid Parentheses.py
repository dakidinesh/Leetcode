"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false"""

#Solution:
class Solution:
    def isValid(self, s: str) -> bool:
        a={')':'(', '}':'{',']':'['}
        b=[]

        for i in s:
            if i in a:
                if b and a[i]==b[-1]:
                    b.pop()
                else:
                    return False
            else:
                b.append(i)
        if not b :
            return True
        return False
        