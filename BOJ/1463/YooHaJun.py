n = int(input())

# index를 1로 만들기 위해 필요한 최소 연산 횟수가 기록된 리스트 = memoization
d = [0] * (n+1)

# 2부터 리스트를 채운다
for i in range(2, n+1):

    # 먼저 현재의 수에서 1을 뺀 경우의 수를 리스트 i 인덱스에 기록
    d[i] = d[i - 1] + 1

    # 2로 나누어져 떨어진 경우와 비교
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

    # 3으로 나누어 떨어진 경우와 비교
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

print(d[n])