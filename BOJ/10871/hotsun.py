## N 사용 안하고 풀기

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in A:
    if i < X:
        print(i, end= ' ')

#%%
N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):  # N 사용해서 풀기
    if A[i] < X:
        print(A[i], end= ' ')


# %%
