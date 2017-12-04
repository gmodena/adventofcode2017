from itertools import combinations

if __name__ == '__main__':
    valid = 0
    while True:
        try:
            passphrase = input().split()
        except EOFError:
            break
        for combi in combinations(passphrase, 2):
            if sorted(list(combi[0])) == sorted(list(combi[1])):
                break
        else:
            valid += 1
    print(valid)
