class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        def dfs(num):
            if low <= num <= high:
                ans.append(num)
                last = num % 10
                if last == 9:
                    return
                dfs(num * 10 + last + 1)

            elif num < low:
                last = num % 10
                if last == 9:
                    return
                dfs(num * 10 + last + 1)

        for i in range(1, 9):
            dfs(i)

        ans.sort()
        return ans