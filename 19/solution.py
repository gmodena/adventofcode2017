if __name__ == '__main__':
    with open('input.txt') as infile:
        route = []
        for line in infile.readlines():
            route.append(list(line.rstrip('\n')))

    # position
    y = 0
    x = route[y].index('|')
    move = 'down'
    letters = []
    steps = 1
    while True:
        if move == 'down':
            y += 1
        elif move == 'up':
            y -= 1
        elif move == 'left':
            x -= 1
        elif move == 'right':
            x += 1

        if route[y][x] in 'ABCDEFGHIJKLMNOPQRSTUVYWZ':
            letters.append(route[y][x])
        elif route[y][x] == '+':
            if x > 0 and move != 'right' and route[y][x-1] != ' ':
                print(route[y][x-1])
                move = 'left'
            elif x < len(route[y]) and move != 'left' and route[y][x+1] != ' ':
                move = 'right'
            elif y > 0 and move != 'down' and route[y-1][x] != ' ':
                move = 'up'
            elif y < len(route) and move != 'up':
                move = 'down'
        elif route[y][x] == ' ':
            break
        steps += 1
    print(''.join([l for l in letters]))
    print(steps)
