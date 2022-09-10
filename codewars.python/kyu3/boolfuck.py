import math
from collections import defaultdict


def tape_op(op: str, tape: defaultdict, tape_ptr: int) -> tuple:
    match op:
        case '+':
            tape[tape_ptr] = tape[tape_ptr] ^ 1
        case '>':
            tape_ptr = tape_ptr + 1
        case '<':
            tape_ptr = tape_ptr - 1
    return tape, tape_ptr


def output_bits_to_string(output_bits):
    pad_len = 8 * math.ceil(len(output_bits) / 8)
    padded = output_bits.ljust(pad_len, '0')

    out_str = ''
    for i in range(0, pad_len, 8):
        byte = padded[i:i + 8]
        rev_bytes = byte[::-1]
        out_str = out_str + chr(int(rev_bytes, 2))
    return out_str


def find_closing_bracket(code: str, pc: int) -> int:
    bracket_count = 1
    while bracket_count > 0:
        pc = pc + 1
        if code[pc] == '[':
            bracket_count += 1
        if code[pc] == ']':
            bracket_count -= 1
    return pc


def back_to_open_bracket(code, pc):
    bracket_count = 1
    while bracket_count > 0:
        pc = pc - 1
        if code[pc] == '[':
            bracket_count -= 1
        if code[pc] == ']':
            bracket_count += 1
    return pc


def boolfuck(code, input_stream=''):
    output_stream = ''
    charlist = list(input_stream)
    input_stream = [int(bit) for bitlist in [list(bin(ord(x))[2:].zfill(8)[::-1]) for x in charlist] for bit
                    in bitlist]
    tape = defaultdict(int)
    tape_ptr = 0
    pgm_len = len(code)
    pc = 0
    while pc < pgm_len:
        instr = code[pc]
        if instr in '+<>':
            tape, tape_ptr = tape_op(instr, tape, tape_ptr)
        if instr == ',':
            tape[tape_ptr] = 0 if len(input_stream) == 0 else input_stream.pop(0)
        if instr == ';':
            output_stream += str(tape[tape_ptr])
        if instr == '[' and tape[tape_ptr] == 0:
            pc = find_closing_bracket(code, pc)
        if instr == ']' and tape[tape_ptr] == 1:
            pc = back_to_open_bracket(code, pc)
        pc = pc + 1
    return output_bits_to_string(output_stream)
