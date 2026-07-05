class Solution(object):
    def pathsWithMaxScore(self, board):
        MOD=10**9+7
        n=len(board)
        dp=[[[-1,0] for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1]=[0,1]
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if board[i][j]=='X' or (i==n-1 and j==n-1):
                    continue
                best=-1
                ways=0

                for ni,nj in ((i+1,j),(i,j+1),(i+1,j+1)):
                    if 0<=ni<n and 0<=nj<n:
                        score,cnt=dp[ni][nj]
                        if cnt==0:
                            continue
                        if score>best:
                            best=score
                            ways=cnt
                        elif score==best:
                            ways=(ways+cnt)%MOD
                    if ways==0:
                        continue
                    val=0 if board[i][j] in "SE" else int(board[i][j])
                    dp[i][j]=[best+val,ways]
        return dp[0][0] if dp[0][0][1] else [0,0]

