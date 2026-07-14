class Solution(object)
    def finalPrices(self, prices)
        stack=[]
        for i in range(len(prices))
            while stack and prices[i]=prices[stack[-1]]
                idx=stack.pop()
                prices[idx]-=prices[i]
            stack.append(i)
        return prices