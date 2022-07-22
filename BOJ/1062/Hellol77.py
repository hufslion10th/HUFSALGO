from itertools import combinations # 라이브러리 itertools 에서 combinations 를 import 해줍니다.
import sys
N,K = map(int,input().split())
# A=[]
# for i in range(N):
#     x=input()
#     y=x[4:-4]
#     A.append(x)
A=[sys.stdin.readline().rstrip()[4:-4] for _ in range(N)] # 시간초과가 나서 


answer=0
already={'a','n','t','i','c'}  # 처음에 무조건 배워야하는 알파벳 5가지
remain = set(chr(i) for i in range(97, 123)) - already # 처음 무조건 배워야하는 알파벳 5가지를 뺀 남은 알파벳 
# remain = set(chr(i+97) for i in range(0,26)) - already 이것을 썼을때에는 시간초과가 났는데 위 코드로 바꾸니까 통과가 되네요.
# chr() 함수는 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환하는 함수입니다.
# ord() 함수는 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
# 97부터 'a' 입니다. ord('a')=97  chr(97)='a' 입니다.
def a(A,learn): # 처음에는 함수코드를 사용 안하고 global코드를 이용했습니다. 하지만 시간초과로 함수코드로 옮겨봤습니다.
    c=0
    for word in A:
        flag=1 # flag를 잡아줍니다.
        for w in word:
            if learn[ord(w)]==0: 
            # 만약 단어들중에 배우지 않는 알파벳이 있다면 읽지 못하는 단어이므로 c에 1을 늘리지 않도록 flag를 0으로 합니다.
                flag=0
                break
        if flag==1:  # 이 지점까지 flag가 1 일때 읽을수 있다는 것이므로 c를 1 늘려줍니다.
            c+=1
    return c


if K>=5:
    learn=[0]*123
    for i in already:
        learn[ord(i)]=1             # 무조건 배워야하는 알파벳 5가지를 배웁니다.
    for j in list(combinations(remain,K-5)): # 무조건 배워야하는 알파벳 5가지를 뺀 K-5개 를 사용해 단어를 읽어야 합니다.
        for k in j: 
            learn[ord(k)]=1 # 알파벳을 배우는 과정
        c=a(A,learn)
        
        if c>answer:
            answer=c
        for k in j :
            learn[ord(k)]=0 # learn 리스트를 처음 상태로 되돌려 놓습니다.          
    print(answer)       
else:
    print(0)


