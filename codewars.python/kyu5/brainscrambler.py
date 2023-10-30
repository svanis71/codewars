"""
https://www.codewars.com/kata/56941f177c0a52aef50000a2/train/python
"""


class Interpreter:
    def __init__(self):
        self.stacks = [[0] for _ in range(3)]

    @staticmethod
    def extract_input_number(code: str, pc: int) -> tuple[int, int]:
        tmp: str = ''
        while True:
            tmp += code[pc]
            if pc < len(code) - 1 and code[pc + 1].isnumeric():
                pc += 1
            else:
                break
        return (int(tmp)), pc

    def read(self, code: str) -> str:
        output_stream, pc = '', 0
        loop_idx = []

        while pc < len(code):
            current_stack = self.stacks[0]
            match code[pc]:
                case '*':
                    current_stack.append(0)
                case '.':
                    if len(current_stack) != 0:
                        output_stream += str(current_stack[-1])
                case '+':
                    if len(current_stack) != 0:
                        current_stack[-1] += 1
                    else:
                        current_stack.append(0)
                case '-':
                    if len(current_stack) != 0:
                        current_stack[-1] -= 1
                    else:
                        current_stack.append(0)
                case '#':
                    self.stacks.append(self.stacks.pop(0))
                case '<':
                    if len(current_stack) != 0:
                        self.stacks[-1].append(current_stack.pop())
                case '>':
                    if len(current_stack) != 0:
                        self.stacks[1].append(current_stack.pop())
                case '^':
                    if len(current_stack) != 0:
                        current_stack.pop()
                case ',':
                    pc += 1
                    input_val, pc = self.extract_input_number(code, pc)
                    current_stack.append(input_val)
                case '[':
                    loop_idx.append(pc)
                case ']':
                    if len(current_stack) > 0 and current_stack[-1] > 0:
                        pc = loop_idx[-1]
                    else:
                        loop_idx.pop()
            pc += 1
        return output_stream
