from math import floor

def is_clean(node):
    if node == '.':
        return True
def prettyprint(m, i, j):
    for k, row in enumerate(m):
        print(k, ' '.join([w for w in row]))
if __name__ == '__main__':
    m = []
    with open('input.txt') as infile:
        for line in infile:
            m.append(list(line.strip()))

    center = floor(len(m) / 2)

    turn = 0
    facing = 0 # 0 up 1 down 2 left 3 right
    i, j = center, center
    infections = 0
    bursts = 10_000
    for time in range(bursts):
        state = ""
        if m[i][j] == '.':
            # turn left
            turn = -1
            state = '#'
            infections += 1
        elif m[i][j] == '#':
            # turn right:
            turn = 1
            state = '.'

        m[i][j] = state
        #print('facing: ', facing, 'turn: ', turn, 'i: ', i, 'j: ', j)
        if facing == 0 and turn == -1:
            # facing up, turn left
            j -= 1
            facing = 2 # face left
        elif facing == 0 and turn == 1:
            # facing up, turn right
            j += 1
            facing = 3 # face right
        elif facing == 1 and turn == -1:
            # facing down, turn left
            j += 1
            facing = 3
        elif facing == 1 and turn == 1:
            j -= 1
            facing = 2 #face left
        elif facing == 2 and turn == -1:
            # facing left, turn left
            i += 1
            facing = 1 # face down
        elif facing == 2 and turn == 1:
            # facing left, turn right
            i -= 1
            facing = 0 # face up
        elif facing == 3 and turn == -1:
            # facing right. turn left
            i -= 1
            facing = 0 # face up
        elif facing == 3 and turn == 1:
            i += 1
            facing = 1 # face down

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
        #prettyprint(m, i, j)
        #print('moved to', i, j)

    prettyprint(m, i, j)
    print(time, infections)
