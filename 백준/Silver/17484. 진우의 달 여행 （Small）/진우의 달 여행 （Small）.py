import sys
def dfs(i, j, except_d, value):
    global mmin
    if value > mmin:
        return
    if i == N - 1:
        mmin = min(mmin, value)
        return
    for k in range(3):
        if k != except_d:
            tmp = j + d[k]
            if 0 <= tmp < M:
                dfs(i + 1, tmp, k, value + board[i + 1][tmp])



N, M = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(N))
d = [-1, 0, 1]
mmin = N * 100

for m in range(M):
    for k in range(3):
        tmp = m + d[k]
        if 0 <= tmp < M:
            dfs(1, tmp, k, board[0][m] + board[1][tmp])

print(mmin)