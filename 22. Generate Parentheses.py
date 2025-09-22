"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def backtracking(opened,closed):
            if opened==closed==n:
                res.append("".join(stack))
                return
            if opened<n:
                stack.append('(')
                backtracking(opened+1,closed)
                stack.pop()
            if closed<opened:
                stack.append(')')
                backtracking(opened,closed+1)
                stack.pop()
        backtracking(0,0)
        return res