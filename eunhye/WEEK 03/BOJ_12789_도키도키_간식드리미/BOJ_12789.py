from collections import deque

N = int(input())
queue = deque(map(int, input().split()))
stack = []

for order in range(1, N + 1):
    if queue and queue[0] == order:
        queue.popleft()
    elif stack and stack[-1] == order:
        stack.pop()
    else:
        while queue:
            if queue[0] == order:
                queue.popleft()
                break
            stack.append(queue.popleft())
        else:
            print("Sad")
            break
else:
    print("Nice")
