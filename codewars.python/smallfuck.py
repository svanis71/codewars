def find_matching_close_bracket(code, start_pos):
    bracket_cnt, pc = 1, start_pos
    while bracket_cnt > 0 and pc < len(code):
        pc += 1
        if code[pc] == '[':
            bracket_cnt += 1
        if code[pc] == ']':
            bracket_cnt -= 1
    return pc


def find_matching_open_bracket(code, start_pos):
    bracket_cnt, pc = 1, start_pos
    while bracket_cnt > 0 and pc >= 0:
        pc -= 1
        if code[pc] == '[':
            bracket_cnt -= 1
        if code[pc] == ']':
            bracket_cnt += 1
    return pc + 1


def interpreter(code, tape):
    """
    https://www.codewars.com/kata/58678d29dbca9a68d80000d7/train/python

    :param code:
    :param tape:
    """
    pc, pointer = 0, 0
    bits = [int(x) for x in tape]
    while (0 <= pointer < len(bits)) and pc < len(code):
        match code[pc]:
            case '>':
                pc += 1
                pointer += 1
            case '<':
                pc += 1
                pointer -= 1
            case '*':
                bits[pointer] = ~bits[pointer] & 1
                pc += 1
            case '[':
                pc = pc + 1 if bits[pointer] == 1 else find_matching_close_bracket(code, pc)
            case ']':
                pc = pc + 1 if bits[pointer] == 0 else find_matching_open_bracket(code, pc)
            case _:
                pc += 1
    return ''.join(str(x) for x in bits)
