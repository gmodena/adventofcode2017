from collections import defaultdict

registers = defaultdict(int)

instructions = {}
instructions['<'] = lambda x, y: x < y
instructions['>'] = lambda x, y: x > y
instructions['>='] = lambda x, y: x >= y
instructions['<='] = lambda x, y: x <= y
instructions['=='] = lambda x, y: x == y
instructions['!='] = lambda x, y: x != y
instructions['inc'] = lambda x, y: x + y
instructions['dec'] = lambda x, y: x - y

def cmp(lhs, cond, rhs):
    op = instructions[cond]
    return op(registers[lhs], int(rhs))
def setr(register, op, value):
    op = instructions[op]
    registers[register] = op(registers[register], int(value))

if __name__ == '__main__':
    max_value = 0
    while True:
        if len(registers) > 0:
            curr_max = sorted(registers.values())[-1]
            if curr_max > max_value:
                max_value = curr_max
        try:
            instruction = input()
            operation, condition = instruction.split('if')
            register, op, value = operation.strip(' ').split(' ')
            lhs, cond, rhs = condition.strip(' ').split(' ')

            if cmp(lhs, cond, rhs):
                setr(register, op, value)
        except EOFError:
            break
    print(sorted(registers.values())[-1])
    print(max_value)
