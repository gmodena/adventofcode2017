if __name__ == '__main__':
    valid = 0
    while True:
        try:
            passphrase = input().split()
        except EOFError:
            break
        if len(set(passphrase)) == len(passphrase):
            valid += 1
    print(valid)
