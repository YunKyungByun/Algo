import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [0] * (max(arr) + 1)
start, end = 0, 0
mmax = 0

while end < N:
    if cnt[arr[end]] < K:
        cnt[arr[end]] += 1
        end += 1
    else:
        flag = False
        cnt[arr[start]] -= 1
        start += 1
    mmax = max(mmax, end - start)
print(mmax)