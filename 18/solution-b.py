registers = [defaultdict(int), defaultdict(int)]

def get_value(registers, v):
    try:
        return int(v)
    except ValueError:
        return registers[v]

if __name__ == '__main__':
    op = 0; reg = 1; val = 2
    with open('input.txt') as infile:
        instructions = [line.strip().split(' ') for line in infile]
    pid = 0
    eip = [0, 0]
    lock = [False, False]
    messages = [[], []]
    registers[0]['p'] = 0
    registers[1]['p'] = 1

    count = 0
    while not (lock[0] and lock[1]):
        pid = (pid+1) % (len(eip))
        if len(instructions) <= eip[pid] < 0:
            break
        ins = instructions[eip[pid]]
        if ins[op] == 'snd':
            messages[pid].append(get_value(registers[pid], ins[reg]))
            if pid == 1:
                count += 1
        elif ins[op] == 'set':
            registers[pid][ins[reg]] = get_value(registers[pid], ins[val])
        elif ins[op] == 'add':
            registers[pid][ins[reg]] += get_value(registers[pid], ins[val])
        elif ins[op] == 'mul':
            registers[pid][ins[reg]] *= get_value(registers[pid], ins[val])
        elif ins[op] == 'mod':
            registers[pid][ins[reg]] %= get_value(registers[pid], ins[val])
        elif ins[op] == 'rcv':
            sender_pid = (pid+1) % (len(eip))
            try:
                registers[pid][ins[reg]] = messages[sender_pid].pop(0)
                lock[pid] = False
            except IndexError:
                lock[pid] = True
                continue
        elif ins[op] == 'jgz':
            reg_value = get_value(registers[pid], ins[reg])
            if reg_value > 0:
                eip[pid] += get_value(registers[pid], ins[val])
                continue
        eip[pid] += 1
    print(count)

