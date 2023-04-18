def solution(keymaps, targets):
    answer = []
    key_dict = dict()

    for keymap in keymaps:
        for i, ch in enumerate(keymap, 1):
            if not ch in key_dict:
                key_dict[ch] = i
            elif key_dict[ch] > i:
                key_dict[ch] = i

    for target in targets:
        click = 0
        for ch in target:
            if ch in key_dict:
                click += key_dict[ch]
            else:
                click = -1
                break

        answer.append(click)

    return answer