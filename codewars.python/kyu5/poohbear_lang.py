import math
from collections import defaultdict


class Program:
    instruction_set_navigate = {
        '>': lambda cell_ptr_pos: cell_ptr_pos + 1,
        '<': lambda cell_ptr_pos: cell_ptr_pos - 1,
    }

    instruction_set_arithmetic = {
        '+': lambda x: (x + 1) % 256,
        '-': lambda x: (x - 1) % 256,
        'L': lambda x: (x + 2) % 256,
        'T': lambda x: (x * 2) % 256,
        'Q': lambda x: (x * x) % 256,
        'I': lambda x: (x - 2) % 256,
        'V': lambda x: int(x / 2),
        'U': lambda x: int(math.sqrt(x)),
    }

    instruction_set_copy_paste = {
        'c': lambda x, buf: buf.copy(x),
        'p': lambda x, buf: buf.buf,
        'A': lambda x, buf: x + buf.buf,
        'B': lambda x, buf: x - buf.buf,
        'Y': lambda x, buf: x * buf.buf,
        'D': lambda x, buf: int(x / buf.buf),
    }

    instruction_set_output = {
        'N': lambda x: str(x),
        'P': lambda x: chr(x),
    }

    def __init__(self):
        self.cells = defaultdict(int)
        self.cell_ptr = 0
        self.output = ''
        self.copy_buf = CopyBuffer()

    def _exec_instruction(self, instr: str):
        if instr in self.instruction_set_arithmetic:
            self.cells[self.cell_ptr] = self.instruction_set_arithmetic[instr](self.cells[self.cell_ptr])
        if instr in self.instruction_set_navigate:
            self.cell_ptr = self.instruction_set_navigate[instr](self.cell_ptr)
        if instr in self.instruction_set_output:
            self.output += self.instruction_set_output[instr](self.cells[self.cell_ptr])
        if instr in self.instruction_set_copy_paste:
            self.cells[self.cell_ptr] = self.instruction_set_copy_paste[instr](self.cells[self.cell_ptr], self.copy_buf)
        return

    def loop(self, code: str, pc: int) -> int:
        loop_end = code.find('E', pc)
        loop_code = code[pc + 1:loop_end]
        while self.cells[self.cell_ptr] != 0:
            for instr in loop_code:
                self._exec_instruction(instr)
        return loop_end

    def _interpret(self, pgm: str) -> str:
        pgm = pgm
        pgm_len = len(pgm)
        pc = 0
        while pc < pgm_len:
            instr = pgm[pc]
            if instr == 'W':
                pc = self.loop(pgm, pc)
            else:
                self._exec_instruction(instr)
                pc = pc + 1

        return self.output

    def interpret(self, pgm: str) -> str:
        return self._interpret(pgm)


class CopyBuffer:
    def __init__(self):
        self._buf = 0

    @property
    def buf(self):
        return self._buf

    def copy(self, x):
        self._buf = x
        return x


def poohbear(pgm: str) -> str:
    """
    https://www.codewars.com/kata/59a9735a485a4d807f00008a/python
    Implementation of the poohbear language (https://esolangs.org/wiki/Poohbear)
    :param pgm: The program
    :return: The output string
    """
    program = Program()
    return program.interpret(pgm)
