from collections import defaultdict


# https://www.codewars.com/kata/58817056e7a31c2ceb000052/train/python
def interpreter(tape: str) -> str:
    pc, tape_len = -1, len(tape)
    data, selector, output = defaultdict(int), 0, ''
    while True:
        pc = (pc + 1) % tape_len
        match tape[pc]:
            case '>':
                selector += 1
            case '<':
                selector -= 1
            case '+':
                data[selector] = (data[selector] + 1) % 256
            case '-':
                data[selector] = 255 if data[selector] == 0 else (data[selector] - 1)
            case '*':
                output += chr(data[selector])
            case '&':
                return output
            case '/':
                pc = pc if data[selector] != 0 else (pc + 1) % tape_len
            case '\\':
                pc = pc if data[selector] == 0 else (pc + 1) % tape_len
