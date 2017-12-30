from copy import copy

def rotate90(m):
    return list(map(list, zip(*m[::-1])))

def fliplr(m):
    return list(reversed(m))

def flipup(m):
    return [list(reversed(x)) for x in m]

def rotate(m):
    rot = []
    for i in range(3):
        m = rotate90(m)
        rot.append(m)
    return rot

def transform(m):
    return rotate(m) + flipup(m) + fliplr(m) + rotate(flipup(m)) + rotate(fliplr(m))

def to_matrix(s):
    m = []
    for row in s.split('/'):
        m.append(list(row))
    return m

def match(m, book):
    m = transform(m)
    for i, rule in enumerate(book):
        if to_matrix(rule[0]) in m:
            return rule[1]

def fractal(m, book, size, enhanced_size):
    new_m_size = enhanced_size * len(m) // size
    new_m = [ ['.'] * new_m_size for _ in range(new_m_size) ]

    ei = 0
    for i in range(0, len(m), size):
        ej = 0
        for j in range(0, len(m), size):
            enhanced = []
            for r in m[i:i+size]:
                enhanced.append(r[j:j+size])
            enhanced = to_matrix(match(enhanced, book))
            for ii in range (len(enhanced)):
                for jj in range(len(enhanced)):
                    new_m[ei+ii][ej+jj] = enhanced[ii][jj]
            ej += enhanced_size
        ei += enhanced_size
    return new_m

def run(n, m, book):
    for it in range(n):
        if len(m) % 2 == 0:
            m = fractal(m, book, 2, 3)
        else:
            m = fractal(m, book, 3, 4)

    s = 0
    for row in m:
        s += row.count('#')
    return s
if __name__ == '__main__':
    m = [['.', '#', '.'],
         ['.', '.', '#'],
         ['#', '#', '#']]

    book = []
    with open('input.txt') as infile:
        for line in infile:
            line = line.rstrip('\n')
            pattern, enhance = line.split(' => ')
            book.append((pattern, enhance))

    # part 1
    print(run(5, copy(m), book))
    # part 2
    print(run(18, copy(m), book))
