'''
__문제 풀이 아이디어__ 는 다음과 같다
- 8개의 지정 방향 벡터 (나이트의 이동 경우의 수)
- DFS 전용 데크(deque)를 선언
  - `pop`와 `append`를 이용 -> LIFO 형식으로 DFS 구현
- 좌표에 이동 횟수 카운터를 기록하기
  - 다음 좌표로 이동했을 때 방문한 적이 없을 경우만 카운터를 증가시키고
  - 이동한 좌표를 데크(deque)에 추가
  - 만약 이동 카운트가 기록된 최솟값 min_val보다 많을 때는 탐색 중지

- 목적지에 도착했을 때 좌표에 기록된 이동횟수 출력

- 본 문제를 DFS로 풀었을 때는 최소 경우의 수가 보장이 되지 않는다고 하는데
- 그 이유를 잘 모르겠습니다.
- 최소값을 비교하면서 탐색했는데 왜 안될까요?
'''

# 나이트가 이동할 수 있는 방향 벡터
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

def dfs():
    global min_val
    queue = list()
    # 시작점
    queue.append((a, b))

    while queue :
        # 가장 오른쪽에 있는 것 pop
        x, y = queue.pop()

        # 이동 카운트가 기록된 최솟값 min_val보다 많을 때는 탐색 중지
        if visited[x][y] > min_val:
            continue

        # 도착했을 때
        if x == c and y == d :
            if visited[x][y] < min_val:
                min_val = visited[x][y]

        for step in steps :
            nx = x + step[0]
            ny = y + step[1]

            # 유효성 검증  0 ~ n-1
            if nx < 0 or ny < 0 or nx >= n or ny >= n :
                continue


            if not visited[nx][ny] :

                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


test_num = int(input())

for _ in range(test_num):
    n = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    visited = [[0] * n for _ in range(n)]
    # 최소값 선언
    min_val = float('inf')
    dfs()
    print(min_val)
