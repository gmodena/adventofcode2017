from collections import defaultdict

registers = defaultdict(int)

def get_value(registers, v):
    try:
        return int(v)
    except ValueError:
        return registers[v]

if __name__ == '__main__':
    op = 0; reg = 1; val = 2
    with open('input.txt') as infile:
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
    print(count)
