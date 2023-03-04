from collections import deque


n = int(input())
students = map(int, input().split())
students = deque(students)

stack = list()
chk_num = 1

while students:
    student = students.popleft()

    if chk_num == student:
        chk_num += 1
    else:
        stack.append(student)

    while stack:
        if stack[-1] == chk_num:
            stack.pop()
            chk_num += 1
        else:
            break

print("Nice") if len(stack) == 0 else print("Sad")