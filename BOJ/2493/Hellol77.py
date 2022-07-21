N=int(input())
A=list(map(int,input().split()))
S=[] # 정답 리스트
Stack=[] # stack


# enumerate 를 사용해서 index도 같이 stack에 넣어주어 어느 탑에서 수신하는지 찾는다. 탑의 번호를 위해 start=1로 한다.
for i in enumerate(A,start=1): 
    # Stack에 아무것도 없으면 레이저 신호를 수신하는 탑이 없다
    if len(Stack)==0: #
        Stack.append(i)
        S.append(0)
    else:
        # 일단 stack안에 들어있는 값이 비교하는 값보다 작으면 더 이상 Stack안에 있는 값은 더 이상 쓸모없는 탑이 되버리기 때문에 pop해준다.
        while Stack[-1][1]<i[1]:
            Stack.pop()
            # pop했을때 Stack안에 아무 값도 없다면 레이저 수신호를 수신하는 탑이 존재하지 않다는 의미
            if len(Stack)==0:
                # Stack 에 append 하여 앞으로 오른쪽의 탑들이 보내는 레이저를 수신할 수 있는지..
                Stack.append(i)
                S.append(0)
                break
        # Stack안에 들어있는 값이 비교하는 값보다 크다면 레이저 신호를 수신하는 탑이 존재한다는 의미        
        if Stack[-1][1]>i[1]:
            # S에 수신받는 탑의 번호를 넣어준다.
            S.append(Stack[-1][0])
            # Stack 에 append 하여 앞으로 오른쪽의 탑들이 보내는 레이저를 수신할 수 있는지..
            Stack.append(i)
        
print(' '.join(map(str,S)))

        
            
    