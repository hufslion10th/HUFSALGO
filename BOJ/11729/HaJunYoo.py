number = int(input())

cnt = 0
def hanoi(num, start, end):
    global cnt

    if num == 0:
        return

    else :
        mid = 6-start-end
        hanoi(num-1, start, mid)
        print(f'{start} {end}')
        cnt+=1
        hanoi(num-1, mid, end)

print(2**number -1)
hanoi(number, 1, 3)
# 아 장대가 3개구나....
