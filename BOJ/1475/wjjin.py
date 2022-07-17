import math # 올림 계산을 위한 math 함수를 호출합니다.

room_num = input() # 문제에서 필요로 하는 방 넘버를 입력받습니다. 

li = list(range(10)) # 문제 해결을 위해 0~9의 숫자를 key로 갖는 딕셔너리를 정의할 것입니다. 이를 위한 key의 리스트 정의입니다.
x = {key: 0 for key, value in dict.fromkeys(li).items()} # key 값으로 0~9, value 값으로 0을 갖는 딕셔너리를 정의합니다.

for i in range(len(room_num)): # 위에서 입력받은 방 넘버를 하나씩 받아서 해당하는 key 값이 있으면 1씩 더하는 for문을 정의합니다.
    x[int(room_num[i])] += 1 # 위에서 input으로 room_num가 index를 가지는 문자열 이므로 이를 이용해서 for문을 작성합니다.

x[6] = math.ceil((x[6] + x[9])/2) # 문제에서 6과 9의 카드가 같이 사용 가능 하다고 했으므로 다른 숫자 카드에 비해 절반의 가치를 가집니다. 이를 하나로 통일해 주고 카드 세트의 경우 정수개로 떨어지므로 이를 위한 올림함수를 사용해줍니다.
# del(x[9]) # 숫자 6과 9의 가치를 통일해 주었으므로 삭제하는 과정을 넣었었는데, 결론 도출에 아무런 영향을 미치지 않아 주석처리 하였습니다.

ans = [v for k,v in x.items() if max(x.values()) == v] # 만들어진 딕셔너리에서 value가 최대인 value 가져옵니다.

print(ans[0]) #정답을 출력합니다.