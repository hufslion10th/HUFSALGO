from collections import deque
import sys
n,m=map(int,sys.stdin.readline().split())
G=[]

for i in range(n):
    G.append(list(map(int,sys.stdin.readline().split())))

# 좌표
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def BFS(G,a,b):
    Q=deque()
    Q.append((a,b))
    G[a][b]=0 # 방문했기 때문에 0으로 바꿔준다.
    count=1
    while Q: # Q에 값이 있다면 반복
        x,y=Q.popleft() #왼쪽에서 빼준다.
        for i in range(4): # 4방향 탐색
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m :
                continue
            if G[nx][ny]==1:
                G[nx][ny]=0 #  방문 했기 때문에 0으로 바꿔준다.
                Q.append((nx,ny))
                count+=1 # 제일 큰 넓이를 찾기 위해서
    return count
    
answer=[]
for i in range(n):
    for j in range(m):
        if G[i][j]==1:  # G를 살펴가면서 1이 시작하는 곳 부터 dx,dy좌표를 이용해서 살펴본다.
            answer.append(BFS(G,i,j))
            
if len(answer)==0: # 그림이 아예 없다면
    print(0)
    print(0)   
else:           
    print(len(answer)) # answer의 길이가 그림의 수가 된다.
    print(max(answer)) # answer의 최댓값이 그림들 중 가장 넓은 그림의 넓이이다.
