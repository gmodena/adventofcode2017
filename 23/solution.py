from collections import defaultdict
from math import sqrt

def part1():
    registers = defaultdict(int)

    def get_value(registers, v):
        try:
            return int(v)
        except ValueError:
            return registers[v]
    op = 0; reg = 1; val = 2
    with open('input.opt.txt') as infile:
        instructions = [line.strip().split(' ') for line in infile]

    count = 0
    pc = 0
    while 0 <= pc < len(instructions):
        ins = instructions[pc]
        if ins[op] == 'set':
            registers[ins[reg]] = get_value(registers, ins[val])
        elif ins[op] == 'sub':
            registers[ins[reg]] -= get_value(registers, ins[val])
        elif ins[op] == 'mul':
            registers[ins[reg]] *= get_value(registers, ins[val])
            count += 1
        elif ins[op] == 'jnz':
            reg_value = get_value(registers, ins[reg])
            if reg_value != 0:
                pc += get_value(registers, ins[val])
                continue
        pc += 1
    return count

def part2():
    def is_prime(n):
        for i in range(2, int(sqrt(n))):
            if n % i == 0:
                return False
        return True

    c = 123700
    h = 0
    for b in range(106700, c+1, 17):
        if not is_prime(b):
            h += 1
    return h

if __name__ == '__main__':
    print(part1())
    print(part2())
