if __name__ == '__main__':
    with open('input.txt', 'r') as infile:
        instructions = list(map(int, infile.readlines()))

    offset = 0
    step = 0

    while offset < len(instructions):
        jump = instructions[offset] + offset
        instructions[offset] += 1
        offset = jump
        step += 1
    print(step)

