H,W=map(int,input().split())
A=list(map(int,input().split()))
ans=0

for i in range(1,W-1): # 양 끝은 물이 차오를수 없으므로 인덱스 범위는 1~W-2 
    l=max(A[:i]) # i에서 부터 왼쪽 끝까지의 블록중 가장 큰수
    r=max(A[i:]) # i에서 부터 오른쪽 끝까지의 블록중 가장 큰수
    
    k=min(l,r) # 둘중 작은 블록의 수
    
    if A[i]<k: # i 지점에 쌓여있는 블록보다 k가 커야 물이 고일수 있습니다.
        ans+=k-A[i]
print(ans)