def part1(n: int) -> int:
    buffer = [0]
    it = 2017
    pos = 0
    for val in range(1, it+1):
        pos = (pos + n) % len(buffer) + 1
        buffer.insert(pos, val)
    return buffer[pos+1]

def part2(n: int) -> int:
    it = 50_000_000
    pos = 0
    buffer = [0]
    lookahed = 0
    for val in range(1, it+1):
        pos = (pos + n) % val+1
        if pos == 1:
            lookahead = val
    return lookahead

if __name__ == '__main__':
    n = 355
    print(part1(n))
    print(part2(n))

