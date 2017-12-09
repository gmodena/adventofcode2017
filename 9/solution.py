if __name__ == '__main__':
    score = 0
    garbage = 0
    while True:
        nestedness = 0
        try:
            stream = list(input())
            has_garbage = False
            garbage_start = None
            for pos, char in enumerate(stream):
                if char == '!':
                    stream[pos+1] = None
                elif char == '<' and not has_garbage:
                    has_garbage = True
                    garbage_start = pos
                elif char == '>':
                    has_garbage = False
                    garbage_start = None
                elif char == '{' and not has_garbage:
                    nestedness += 1
                elif char == '}' and not has_garbage:
                    score += nestedness
                    nestedness -= 1

                if has_garbage and char not in ('!', None) and garbage_start < pos:
                    garbage += 1
        except EOFError:
            break
    print(score)
    print(garbage)
