
# [Solution 2]
import sys

def chatbot(N, now):
    # 탈출조건
    if N + now == -1:
        return

    # print(f"\t[process check]\t{now}, {N}, {N + now}")
    # 재귀함수가 뭔가요? 잘 들어보게 
    if 0 <= now < N:
        print(str(now * depths) + question_1)
        print(str(now * depths) + question_2)
        print(str(now * depths) + question_3)
        print(str(now * depths) + question_4)
        return chatbot(N, now + 1)
    
    # 재귀함수는 자기 자신을 호출하는 함수라네
    if now == N:
        print(str(now * depths) + question_1)
        print(str(now * depths) + answer)
        print(str(now * depths) + close)
        return chatbot(N, now = -1)
    
    # 라고 답변하였지.
    if now < 0:
        print(str((N + now) * depths) + close)
        return chatbot(N, now - 1)


def main():
    
    # 입력
    N = int(sys.stdin.readline().strip())

    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
    chatbot(N, now = 0)

if __name__ == "__main__":

    # 출력값 초기화
    question_1 = "\"재귀함수가 뭔가요?\""
    question_2 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
    question_3 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
    question_4 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
    depths = "____"
    answer = "\"재귀함수는 자기 자신을 호출하는 함수라네\""
    close = "라고 답변하였지."

    main()
