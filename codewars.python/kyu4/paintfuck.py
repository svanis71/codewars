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


def interpreter(code, iterations, width, height):
    code = ''.join(c for c in code if c in '[*]nesw')
    cellx, celly, iterno, pc = 0, 0, 0, 0
    cells = [[0 for _ in range(width)] for _ in range(height)]
    while iterno < iterations and pc < len(code):
        if code[pc] == '[':
            pc = pc + 1 if cells[celly][cellx] == 1 else find_matching_close_bracket(code, pc) + 1
        elif code[pc] == ']':
            pc = pc + 1 if cells[celly][cellx] == 0 else find_matching_open_bracket(code, pc)
        else:
            match code[pc]:
                case '*':
                    cells[celly][cellx] ^= 1
                case 'n':
                    celly = celly - 1 if celly > 0 else height - 1
                case 's':
                    celly = (celly + 1) % height
                case 'w':
                    cellx = cellx - 1 if cellx > 0 else width - 1
                case 'e':
                    cellx = (cellx + 1) % width
            pc += 1
        iterno += 1
    return '\r\n'.join([''.join([str(x) for x in y]) for y in cells])
