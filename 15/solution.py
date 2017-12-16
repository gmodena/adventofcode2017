def gen(value, n, factor, mul=1):
    value *= factor
    value %= n

    if (value % mul == 0):
        yield value
    yield from gen(value, n, factor, mul)

def solve(iteration, mul_a=1, mul_b=1):
    factor_a = 16807
    factor_b = 48271
    n = 2147483647
    a = 512
    b = 191
    total = 0
    cnt = 0
    mask = 0xFFFF

    while cnt < iteration:
        a = next(gen(a, n, factor_a, mul_a))
        b = next(gen(b, n, factor_b, mul_b))
        cnt += 1
        if a & mask == b & mask:
            total += 1
    return total

if __name__ == '__main__':
    # part 1
    print(solve(40_000_000))
    # part 2
    print(solve(5_000_000, mul_a=4, mul_b=8))
