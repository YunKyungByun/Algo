import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))
ssum = sum(arr[0:X])
mmax = ssum
cnt = 1

for i in range(N - X):
    ssum = ssum + arr[X + i] - arr[i]
    if mmax < ssum:
        cnt = 1
        mmax = ssum
    elif mmax == ssum:
        cnt += 1

if mmax == 0:
    print("SAD")
else:
    print(mmax)
    print(cnt)