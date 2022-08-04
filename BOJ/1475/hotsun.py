N = [0,1,2,3,4,5,6,7,8,9]  # 선택 가능한 숫자 
sticker = list(map(int, input()))  # 고른 스티커 숫자들을 리스트로 만들어줌 

for i in range(len(sticker)):  # 9가 들어오면 6으로 바꿔주는 반복문 
    if sticker[i] == 9:
        sticker[i] =6

counter = []   # 스티커들의 갯수를 저장하는 리스트 
for j in N:
    if j == 6:  # 6이 들어오는 경우 6은 9로 대체되기 때문에 
        if sticker.count(j) % 2 == 0:  # 짝수이면 
            num = sticker.count(j)//2   # 2로 나눈 값이 필요한 스티커 세트 갯수
        else:
            num = sticker.count(j)//2 + 1   # 홀수이면 
        counter.append(num)  # 2로 나눈 값에서 한 세트 더 필요하기 때문에 +1 해준게 필요한 세트 갯수 
    else:
        num = sticker.count(j)  # 6이나 9가 아닌 경우에는 
        counter.append(num)  # 숫자가 언급된 갯수 == 필요한 스티커 세트의 갯수와 동일 

int(max(counter))  # 이 중 최댓값이 필요한 스티커 셋트의 최솟값이 됨. 