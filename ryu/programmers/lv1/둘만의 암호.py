# z = 122
# a = 97
# 최대 142
#
from collections import deque


def asc_chk(asc):
    asc = (asc - 97) % 26 + 97

    return asc


def solution(s, skip, index):
    answer = ''
    skip_ascs = [asc_chk(ord(ch)) for ch in skip]

    for ch in s:
        ascs = [asc_chk(ord(ch) + i) for i in range(1, index + 1)]
        queue = deque(ascs)

        while queue:
            asc = queue.popleft()
            if asc in skip_ascs:
                if queue:
                    queue.append(asc_chk(queue[-1] + 1))
                else:
                    queue.append(asc_chk(asc + 1))

        answer += chr(asc)

    return answer
