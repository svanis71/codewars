# https://www.codewars.com/kata/58855acc9e1de22dff0000ef
def interpreter(code: str) -> str:
    pos, stack, output = 0, [0], ''
    while pos < len(code):
        match code[pos]:
            case '^':
                stack.pop()
            case '!':
                stack.append(0)
            case '+':
                stack.append((stack.pop() + 1) % 256)
            case '-':
                i = stack.pop() - 1
                stack.append(255 if i < 0 else i)
            case '*':
                output += chr(stack[-1])
            case '[':
                if stack[-1] == 0:
                    pos = code.find(']', pos)
            case ']':
                if stack[-1] != 0:
                    pos = code.rfind('[', pos)
        pos += 1
    return output
