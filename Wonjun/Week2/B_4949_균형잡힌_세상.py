from collections import deque


def main():
    input_string = input()
    while not input_string == ".":
        stack = deque([])
        balance = True
        for i in input_string:
            if i in "([":
                stack.append(i)
            elif i == ")":
                if not stack or stack.pop() != "(":
                    balance = False
                    break
            elif i == "]":
                if not stack or stack.pop() != "[":
                    balance = False
                    break
        print("no" if (stack or not balance) else "yes")
        input_string = input()


if __name__ == "__main__":
    main()


# 두 괄호 종류는 섞일 수 없으며 마지막에 들어온 왼쪽 괄호부터 짝을 찾아 나간다.
# stack을 사용하자.
# (나 [만 나오는 경우를 잡기 위해 if stack을 썼음
# "yes"나 "no"를 return하는 함수를 여러 번 호출하여 답안 리스트를 만든 뒤에 join으로 출력해도 된다.
