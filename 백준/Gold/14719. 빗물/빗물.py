import sys
input = sys.stdin.readline

H, W = map(int, input().split())
arr = list(map(int, input().split()))
res = 0

for i in range(1, W - 1):
    left_top = max(arr[:i])
    right_top = max(arr[i+1:])
    mmin = min(left_top, right_top)

    if mmin > arr[i]:
        res += mmin - arr[i]

print(res)