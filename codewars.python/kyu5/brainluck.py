from collections import defaultdict


def brain_luck(code: str, input: str) -> str:
    '''
    https://www.codewars.com/kata/526156943dfe7ce06200063e/train/python


    :param code: the program code, a string with the sequence of machine instructions
    :param input: the program input, a string, possibly empty, that will be interpreted as an array of bytes using each character's ASCII code and will be consumed by the instruction
    :return: the output of the interpreted code (always as a string), produced by the instruction
    '''
    out_stream = ""
    tape = defaultdict(int)
    tape_ptr = 0
    pc = 0
    input_bytes = [ord(c) for c in input]
    pgm_len = len(code)

    while pc < pgm_len:
        instr = code[pc]
        if instr == '+':
            tape[tape_ptr] = 0 if tape[tape_ptr] == 255 else tape[tape_ptr] + 1
        if instr == '-':
            tape[tape_ptr] = 255 if tape[tape_ptr] == 0 else tape[tape_ptr] - 1
        if instr == '>':
            tape_ptr = tape_ptr + 1
        if instr == '<':
            tape_ptr = tape_ptr - 1
        if instr == ',':
            tape[tape_ptr] = 0 if len(input_bytes) == 0 else input_bytes.pop(0)
        if instr == '.':
            out_stream += chr(tape[tape_ptr])
        if instr == '[':
            if tape[tape_ptr] == 0:
                bracket_count = 1
                while bracket_count > 0:
                    pc = pc + 1
                    if code[pc] == '[':
                        bracket_count += 1
                    if code[pc] == ']':
                        bracket_count -= 1
        if instr == ']':
            if tape[tape_ptr] != 0:
                bracket_count = 1
                while bracket_count > 0:
                    pc = pc - 1
                    if code[pc] == '[':
                        bracket_count -= 1
                    if code[pc] == ']':
                        bracket_count += 1
        pc = pc + 1

    return out_stream
