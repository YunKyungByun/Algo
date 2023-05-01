import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]
lp, rp = 0, 0
answer = 0

while lp != N:
    rp = lp + k
    case = set()
    addable = True
    for i in range(lp, rp):
        i %= N
        case.add(arr[i])
        if arr[i] == c: addable = False

    cnt = len(case)
    if addable: cnt += 1
    answer = max(answer, cnt)
    lp += 1

print(answer)