class Solution(object):
    def compress(self, chars):
        c=1
        ans=[]
        for i in range(1,len(chars)):
            if chars[i]==chars[i-1]:
                c+=1
            else:
                ans.append(chars[i-1])
                if c>1:
                    for d in str(c):

                        ans.append(d)
            
                c=1
        ans.append(chars[-1])
        if c>1:
            
            for d in str(c):

                ans.append(d)
        for i in range(len(ans)):
            chars[i]=ans[i]
        return len((ans))

        