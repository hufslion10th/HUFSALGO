# 제가 처음에 작성한 함수였습니다.
#
# def editor(word, cursor, n):
#     cl = []
#     for _ in range(n):
#         cl.append(sys.stdin.readline().rstrip())
#     for i in cl:
#         if i == 'L':
#             if cursor >= 1: cursor -= 1 
#         elif i == 'D':
#             if cursor <= len(word): cursor += 1
#         elif i == 'B':
#             if not cursor == 0:
#                 del word[cursor - 1] 
#         else:
#             word.insert(cursor, i[2])
#             cursor +=1
#     return word
# 
# cursor위치를 두고 word list에 insert 함수를 사용해서 추가했는데...
# insert 함수의 경우는 O(n)만큼의 시간을 소요한다고 하더군요. 그래서 시간초과가 났었습니다 ㅠㅠ
# 자료구조에 많이 약해서 이번 풀이는 다른사람 풀이를 참고했습니다.

import sys

word = list(sys.stdin.readline().rstrip()) #개행문자를 제거하여 단어 입력을 받습니다.
st = [] # 정답을 담기 위한 스택 

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] =='L':
        if word:
            st.append(word.pop())
    elif command[0] == 'D':
        if st:
            word.append(st.pop())
    elif command[0] == 'B':
        if word:
            word.pop()
    else:
        word.append(command[1])

        
word.extend(reversed(st)) # 스택을 뒤집어서 정답에 extend합니다. st.reverse() 가 아닌 reversed(st) 를 사용한 이유는 모든 명령이 끝난 후 st에 값이 아무것도 존재하지 않는다면 st.reverse() 는 TypeError를 띄우기 때문이라고 합니다.
print(''.join(word))