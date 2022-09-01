import math
from collections import defaultdict


def output_bits_to_string(output_bits):
    pad_len = 8 * math.ceil(len(output_bits) / 8)
    padded = output_bits.ljust(pad_len, '0')

    out_str = ''
    for i in range(0, pad_len, 8):
        byte = padded[i:i + 8]
        rev_bytes = byte[::-1]
        out_str = out_str + chr(int(rev_bytes, 2))
    return out_str


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
        if instr == '+':
            tape[tape_ptr] = tape[tape_ptr] ^ 1
        if instr == '>':
            tape_ptr = tape_ptr + 1
        if instr == '<':
            tape_ptr = tape_ptr - 1
        if instr == ',':
            tape[tape_ptr] = 0 if len(input_stream) == 0 else input_stream.pop(0)
        if instr == ';':
            output_stream += str(tape[tape_ptr])
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
            if tape[tape_ptr] == 1:
                bracket_count = 1
                while bracket_count > 0:
                    pc = pc - 1
                    if code[pc] == '[':
                        bracket_count -= 1
                    if code[pc] == ']':
                        bracket_count += 1
        pc = pc + 1
    return output_bits_to_string(output_stream)
