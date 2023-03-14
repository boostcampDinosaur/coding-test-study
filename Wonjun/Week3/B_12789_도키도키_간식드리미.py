from collections import deque


def main():
    N = input()
    order = deque(map(int, input().split()))  # 지금 서 있는 순서
    side = deque([])  # 옆으로 빠지는 곳
    current_order = 1  # 이번 차례
    while order:  # order가 없어질 때까지 작동
        if order[0] == current_order:  # order 앞의 학생 차례라면
            order.popleft()  # 내보내고
            current_order += 1  # 이번 차례 += 1
        else:  # order 앞의 학생 차례가 아니라면
            if side:  # side를 보자
                if side[-1] == current_order:  # side 맨 앞의 학생 차례라면
                    side.pop()  # 내보내고
                    current_order += 1  # 이번 차례 += 1
                    continue
            side.append(order.popleft())  # side 맨 앞의 학생 차례도 아니라면 order에서 하나 side로 보내기

    while side:  # side가 차 있는 동안에 작동
        if side[-1] == current_order:  # 맨 앞 학생 차례가 맞다면
            side.pop()
            current_order += 1
        else:  # 아니라면 방법이 없음
            print("Sad")
            break

    if not side:  # side까지 모두 비웠다면 성공
        print("Nice")


if __name__ == "__main__":
    main()
