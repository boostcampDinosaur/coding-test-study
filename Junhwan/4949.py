import sys

input = sys.stdin.readline


def solution_per_line(line):
    stack = []
    for character in line:
        if character in ("(", "["):
            stack.append(character)

        elif character == ")":
            if not stack:
                return "no"

            if stack.pop() != "(":
                return "no"

        elif character == "]":
            if not stack:
                return "no"
            if stack.pop() != "[":
                return "no"

        elif character == ".":
            if stack:
                return "no"
            return "yes"


def main():
    while True:
        line = input().rstrip()
        if line == ".":
            break
        print(solution_per_line(line))


if __name__ == "__main__":
    main()
