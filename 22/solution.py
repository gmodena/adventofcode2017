from math import floor

def prettyprint(m, i, j):
    for k, row in enumerate(m):
        print(k, ' '.join([w for w in row]))
if __name__ == '__main__':
    m = []
    with open('sample.txt') as infile:
        for line in infile:
            m.append(list(line.strip()))

    center = floor(len(m) / 2)
    i, j = center, center
    facing = 0 # 0 up 1 down 2 left 3 right
    infections = 0
    bursts = 10_000
    for time in range(bursts):
        if m[i][j] == '.':
            m[i][j] = '#'
            infections += 1
            facing = (facing + 3) % 4
        elif m[i][j] == '#':
            m[i][j] = '.'
            facing = (facing + 1) % 4

        if facing == 0:
            i -= 1
        elif facing == 1:
            j += 1
        elif facing == 2:
            i += 1
        elif facing == 3:
            j -= 1

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

    print(time, infections)
