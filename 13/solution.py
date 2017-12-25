from collections import defaultdict

if __name__ == '__main__':
    layers = {}
    with open('input.txt') as infile:
        for row in infile.readlines():
            x, y = row.strip().split(':')
            layers[int(x.strip())] = int(y.strip())

    severity = 0
    for time in layers:
        layer_pos = time % (2 * (layers[time] - 1))
        if layer_pos == 0:
            severity += time * layers[time]
    print(severity)
