import itertools

if __name__ == '__main__':
    checksum = 0
    while True:
        try:
            numbers = map(int, input().split())
        except EOFError:
            break
        row_sum = 0
        for combi in itertools.combinations(numbers, 2):
            numerator = max(combi)
            denumerator = min(combi)
            if numerator % denumerator == 0:
                row_sum += numerator // denumerator
        checksum += row_sum
    print(checksum)
