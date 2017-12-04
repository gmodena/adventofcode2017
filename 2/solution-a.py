if __name__ == '__main__':
    checksum = 0
    while True:
        try:
            numbers = input()
        except EOFError:
            break
        numbers = map(int, numbers.split('\t'))
        numbers = sorted(numbers)
        checksum += numbers[-1] - numbers[0]
    print(checksum)
