if __name__ == '__main__':
    captcha = input()

    mysum = 0
    prev = captcha[-1]

    for digit in captcha:
        if digit == prev:
            mysum += int(digit)
        prev = digit
    print(mysum)
