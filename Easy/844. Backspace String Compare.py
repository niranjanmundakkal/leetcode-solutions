class Solution(object):
    def build(self,s):
        stack=[]
        for ch in s:
            if ch!="#":
                stack.append(ch)
            elif stack:
                stack.pop()
        return "".join(stack)

    def backspaceCompare(self, s, t):

        return self.build(s) == self.build(t)