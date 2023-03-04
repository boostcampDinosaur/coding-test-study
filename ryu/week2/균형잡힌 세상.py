while True:
    sentence = input()
    if sentence == ".":
        break

    stack = list()

    for s in sentence:
        if s in ["(", "["]:
            stack.append(s)

        if s == ")":
            if not stack:
                stack.append(s)
                break
            if stack[-1] ==  "(":
                stack.pop()
            else:
                stack.append(s)
                break

        if s == "]":
            if not stack:
                stack.append(s)
                break
            if stack[-1] == "[":
                stack.pop()
            else:
                stack.append(s)
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")