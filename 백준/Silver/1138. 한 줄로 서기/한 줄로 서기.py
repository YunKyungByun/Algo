import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 순서 저장할 리스트
line = [0] * N

for i in range(N):
    cnt = 0
    # line 리스트 탐색
    for j in range(N):
        # 빈 자리 탐색
        if line[j] == 0:
           cnt += 1
        # 빈자리를 나보다 큰 숫자가 있는 개수 만큼 세어졌으면
        if cnt == arr[i] + 1:
            line[j] = i + 1
            break

print(*line)