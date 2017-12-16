from typing import List

def spin(lst: List[str], n: int) -> List[str]:
    return lst[-n:] + lst[:-n]

def exchange(lst: List[str], a: int, b: int) -> List[str]:
    lst[b], lst[a] = lst[a], lst[b]
    return lst

def partner(lst: List[str], a: str, b: str) -> List[str]:
    i = lst.index(a)
    j = lst.index(b)
    return exchange(lst, i, j)

def dance(s: str, instructions: List[str]) -> str:
    xs: List[str] = list(s)
    for instruction in instructions:
        if instruction[0] == 's':
            xs = spin(xs, int(instruction[1:]))
        elif instruction[0] == 'x':
            a, b = map(int, instruction[1:].split('/'))
            xs = exchange(xs, a, b)
        else:
            xs = partner(xs, instruction[1], instruction[3])
    return ''.join([c for c in xs])

if __name__ == '__main__':
    s = 'abcdefghijklmnop'

    with open('input.txt') as infile:
        instructions = infile.readline().strip().split(',')
    # part 1
    print(dance(s, instructions))

    # part 2
    cache: List[str] = [s]
    n = 1_000_000_000
    for i in range(1, n):
        s = dance(s, instructions)
        if s in cache:
            break
        cache.append(s)
    print(cache[n % i])


