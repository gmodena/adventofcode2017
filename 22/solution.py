from math import floor
from copy import deepcopy

def prettyprint(m):
    for k, row in enumerate(m):
        print(k, ' '.join([w for w in row]))

def grid_extend(m, i, j):
    if i < 0:
        m.insert(0, ['.']* len(m[0]))
        i = 0
    if i >= len(m):
        m.append(['.'] * len(m[0]))
    if j < 0:
        for k in range(len(m)):
            m[k].insert(0, '.')
        j = 0
    if j >= len(m[0]):
        for k in range(len(m)):
            m[k].append('.')

    return m, i, j

def move(facing, i, j):
    if facing == 0:
        i -= 1
    elif facing == 1:
        j += 1
    elif facing == 2:
        i += 1
    elif facing == 3:
        j -= 1
    return i, j

def part2(m, bursts=10_000_000):
    center = floor(len(m) / 2)
    i, j = center, center
    facing = 0 # 0 up 1 down 2 left 3 right
    infections = 0

    for time in range(bursts):
        if m[i][j] == '.':
            m[i][j] = 'W'
            facing = (facing + 3) % 4
        elif m[i][j] == 'W':
            m[i][j] = '#'
            infections += 1
        elif m[i][j] == '#':
            m[i][j] = 'F'
            facing = (facing + 1) % 4
        elif m[i][j] == 'F':
            m[i][j] = '.'
            facing = (facing + 2) % 4

        i, j = move(facing, i, j)
        m, i, j = grid_extend(m, i, j)
    return infections

def part1(m, bursts=10_000):
    center = floor(len(m) / 2)
    i, j = center, center
    facing = 0 # 0 up 1 down 2 left 3 right
    infections = 0
    for time in range(bursts):
        if m[i][j] == '.':
            m[i][j] = '#'
            infections += 1
            facing = (facing + 3) % 4
        elif m[i][j] == '#':
            m[i][j] = '.'
            facing = (facing + 1) % 4

        i, j = move(facing, i, j)
        m, i, j = grid_extend(m, i, j)
    return infections
if __name__ == '__main__':
    m = []
    with open('input.txt') as infile:
        for line in infile:
            m.append(list(line.strip()))

    print(part1(deepcopy(m)))
    print(part2(deepcopy(m)))
