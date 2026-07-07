class Solution(object):
    def sumAndMultiply(self, n):
        d=[]
        for i in str(n):

            if i!='0':
                d.append(i)
        if not d:
            return 0
        x=int("".join(d))
        dsum=sum(int(i) for i in d)
        return x * dsum
