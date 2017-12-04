if __name__ == '__main__':
    captcha = list(str(input()))

    lookahead = len(captcha) // 2

    prev = captcha[-lookahead]
    cumsum = 0
    for index, digit in enumerate(captcha):
        if prev == digit:
            cumsum += int(digit)
        prev = captcha[(index + lookahead + 1) % len(captcha)]
    print(cumsum)
