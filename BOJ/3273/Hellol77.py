n=int(input())
A=list(map(int,input().split()))
x=int(input())
answer=0
# A 리스트를 정렬해봅니다
A.sort()
left=0
right=n-1

# left가 right 보다 크게 되면 반복을 멈춥니다.
while left<right:
    # 만약 A[left]+A[right]가 x보다 작다면 left에 1을 더해주어서 현재 더한 결과값보다 큰수를 만듭니다.
    if A[left]+A[right]<x:
        left+=1
    # 만약 A[left]+A[right]가 x보다 크다면 right에 1을 빼주어서 현재 더한 결과값보다 작은수를 만듭니다.
    elif A[left]+A[right]>x:
        right-=1
    # 같다면 answer에 1을 더해줍니다. 
    elif A[left]+A[right]==x:
        answer+=1
        # 다른 수들도 찾기 위해서 right에 1을 빼줍니다.
        right-=1
print(answer)

