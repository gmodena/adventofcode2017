if __name__ == '__main__':
    banks = list(map(int, input().split()))

    states = []
    while banks not in states:
        states.append(banks[:])
        blocks = max(banks)
        max_blocks_index = banks.index(blocks)
        banks[max_blocks_index] = 0
        for block in range(max_blocks_index+1, blocks+max_blocks_index+1):
            banks[block % len(banks)] += 1
    print(len(states))
    print(len(states) - states.index(banks))
