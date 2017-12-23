if __name__ == '__main__':
    with open('input.txt') as infile:
        grid = infile.read().strip().split(',')

    x = 0
    y = 0
    z = 0
    distance = []
    for move in grid:
        if move == 's':
            x -= 1
            z += 1
        elif move == 'sw':
            x -= 1
            y += 1
        elif move == 'nw':
            y += 1
            z -= 1
        elif move == 'n':
            z -= 1
            x += 1
        elif move == 'ne':
            x += 1
            y -= 1
        elif move == 'se':
            y -= 1
            z += 1


        distance.append(int((abs(x) + abs(y) + abs(z)) / 2))
    print(int((abs(x) + abs(y) + abs(z)) / 2))
    print(max(distance))
