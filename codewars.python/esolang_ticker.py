from collections import defaultdict


def interpreter(tape):
    selector, memory, output = 0, defaultdict(int), ''
    for c in tape:
        match c:
            case '>':
                selector += 1
            case '<':
                selector -= 1
            case '+':
                memory[selector] = (memory[selector] + 1) % 256
            case '-':
                memory[selector] = (memory[selector] + 1) % 256
            case '/':
                memory[selector] = 0
            case '*':
                output += chr(memory[selector])
    return output
