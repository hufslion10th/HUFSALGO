'''
세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 
이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.
'''

# 조건 1: 한 번에 한 개의 원판을 옮길 수 있다.
# 조건 2: 쌓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다. -> 목적지의 원판이 이동할 원판보다 넓을 경우 (조건) 이동할 수 있다.

# 특정 조건에 의해 작업이 반복되므로 재귀가 쓰일 수 있을 것 같은데
# 조건을 제대로 충족했다는 전제 하에서: 세번째 장대의 원판 너비 합이 sum(n) =====> n == 1 일때를 잡는게 다른 조건 안만들고 더 좋다.


# [reference] [하노이의 탑 이해하기](https://shoark7.github.io/programming/algorithm/tower-of-hanoi)

# 직관의 표현: hanoi(N) = hanoi(N-1) & hanoi(N-1)   # 본 식은 실제 재귀함수의 동작이 아닌 횟수로 이해
# N개를 옮기기 위해서는 N-1 번째를 옮겨야하는데, N-1 번째를 옮기기 위해서는 N-2 번째를 옮겨야하므로 hanoi(n) = n + hanoi(n-1) = n + (n-1) + hanoi(n-2) ... + "1" 이다.

# 경유점이라는 개념: 어디를 거쳐갈 것인지도 중요하다.
# <img width="1095" alt="image" src="https://user-images.githubusercontent.com/60145951/180804848-3136dd5a-748a-480e-860d-1183fa7fa935.png">

# * 경유점 개념이 모호한데 이거 이래도 되나 : 경유점이 다음 재귀에서는 시작점이 되는식? -> 맞는듯*

def hanoi(disk, start, to, via, log):
    if disk == 1:   # 탈출조건
        log.append((start, to))
        return
    
    else:
        hanoi(disk-1, start, via, to, log)
        log.append((start, to))
        hanoi(disk-1, via, to, start, log)

def main():
    # INPUT
    n = int(input())    # 원판

    # OUTPUT
    log = []
    hanoi(n, 1, 3, 2, log)

    print(len(log))
    for move in log:
        start, to = move 
        print(start, to)

if __name__ == "__main__":
    main()