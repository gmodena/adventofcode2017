def is_caught(layers, time, delay=0):
    layer_pos = (time+delay) % (2 * (layers[time] - 1))
    if layer_pos == 0:
        return True
    return False

def part1(layers):
    severity = 0
    for time in layers:
        if is_caught(layers, time):
            severity += time * layers[time]
    return severity

def part2(layers):
    delay = 0
    while True:
        caught = False
        for time in layers:
            if is_caught(layers, time, delay):
                caught = True
                break
        if not caught:
            break
        delay += 1
    return delay

if __name__ == '__main__':
    layers = {}
    with open('input.txt') as infile:
        for row in infile.readlines():
            x, y = row.strip().split(':')
            layers[int(x.strip())] = int(y.strip())
    print(part1(layers))
    print(part2(layers))
