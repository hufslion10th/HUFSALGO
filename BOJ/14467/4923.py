'''
# 소가 길을 건너간 이유 1

문제
닭이 길을 건너간 이유는 과학적으로 깊게 연구가 되어 있지만, 의외로 소가 길을 건너간 이유는 거의 연구된 적이 없다. 이 주제에 관심을 가지고 있었던 농부 존은 한 대학으로부터 소가 길을 건너는 이유에 대한 연구 제의를 받게 되었다.

존이 할 일은 소가 길을 건너는 것을 관찰하는 것이다. 존은 소의 위치를 N번 관찰하는데, 각 관찰은 소의 번호와 소의 위치 하나씩으로 이루어져 있다. 존은 소를 10마리 가지고 있으므로 소의 번호는 1 이상 10 이하의 정수고, 소의 위치는 길의 왼쪽과 오른쪽을 의미하는 0과 1 중 하나다.

이 관찰 기록을 가지고 소가 최소 몇 번 길을 건넜는지 알아보자. 즉 같은 번호의 소가 위치를 바꾼 것이 몇 번인지 세면 된다.

입력
첫 줄에 관찰 횟수 N이 주어진다. N은 100 이하의 양의 정수이다. 다음 N줄에는 한 줄에 하나씩 관찰 결과가 주어진다. 관찰 결과는 소의 번호와 위치(0 또는 1)로 이루어져 있다.

출력
첫 줄에 소가 길을 건너간 최소 횟수를 출력한다.
'''

# Condition
# 관찰 횟수 N은 소의 번호와 소의 위치로 구성된다.
# 소의 번호는 1부터 10 사이의 정수, 소의 위치는 길의 왼쪽 (0) 과 오른쪽 (1) 으로 구성된다.
# 길의 왼쪽과 오른쪽의 차이는 1이다.
# '같은 번호의 소가 위치를 바꾼 것이 몇 번인가?'

import sys

# -- 1. 입력 -- #
# 여러 줄에 걸쳐 입력을 받으므로 input 보다 readlines() 를 사용한다.
N = int(sys.stdin.readline().strip())   # 관찰 횟수

# 선언: 인덱스가 소의 번호다. O(1)으로 접근할 수 있으며 초기값은 0이다.

# 일단 for _ 으로 둔 이상 range 가 1, 11 이든 0, 10 이든 상관이 없다. 10자리만 나오고 그 index는 전부 같기 때문. 차라리 0, 11로 하는게 낫다.
movement_log = [-1 for _ in range(11)]  # 소의 번호와 위치를 연산한 결과
movement_result = [0 for _ in range(11)]    # 길을 건넌 횟수를 기록하는 리스트

# -- 2. 계산 -- #
# 관찰 결과를 입력받으며 위치를 조정

for i in range(N):
    cow_number, current_position = map(int, sys.stdin.readline().strip().split())
    
    # movement_log[cow_number] == -1 일 때는 소를 처음으로 관찰한 때다.
    if movement_log[cow_number] != -1 and movement_log[cow_number] != current_position:
        movement_result[cow_number] += 1    
    movement_log[cow_number] = current_position # 현재 위치로 초기화

# -- 3. 결과 출력 -- #
print(sum(movement_result))




