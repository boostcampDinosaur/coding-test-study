while 1:
    input_str = input()
    if input_str == ".":
        break
    stack = []
    input_str = "".join(input_str.split())
    for ch in input_str:
        if ch == "(" or ch == "[":
            stack.append(ch)
        elif ch == ")":
            if not stack or stack[-1] != "(":
                print("no")
                break
            stack.pop()
        elif ch == "]":
            if not stack or stack[-1] != "[":
                print("no")
                break
            stack.pop()
        else:
            continue
    else:
        if stack:
            print("no")
        else:
            print("yes")
