from typing import List, Tuple
from functools import reduce
from operator import xor

def hexdump(s: List[int]) -> str:
    return ''.join(['{:x}'.format(x).zfill(2)  for x in s])

def myhash(lst: List[int], lenghts: List[int],
           cur: int = 0, skip: int = 0)-> Tuple[List[int], int, int]:
    cur = cur
    skip = skip
    lst_size = len(lst)
    for length in lengths:
        lst_rotated = lst[cur%lst_size:] + lst[:cur%lst_size]
        subl = lst_rotated[0:length]
        subl.reverse()
        lst_rotated[0:length] = subl
        pivot = (lst_size-cur)%lst_size
        lst = lst_rotated[pivot:] + lst_rotated[:pivot]
        cur += length + skip
        skip += 1
    return lst, cur, skip

def knot(lenghts: List[int], rounds: int = 64) -> List[int]:
    lst = list(range(256))
    cur = 0
    skip = 0
    while rounds > 0:
        lst, cur, skip = myhash(lst, lengths, cur=cur, skip=skip)
        rounds -= 1

    dense_hash = [reduce(xor, lst[i:i+16], 0) for i in range(0, len(lst), 16)]
    return dense_hash

def dfs(graph):
    regions = 0
    while graph:
        stack = [graph[0]]
        while stack:
            (i, j) = stack.pop()
            if (i, j) in graph:
                graph.remove((i, j))
                stack.extend([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])
        regions += 1
    return regions


if __name__ == '__main__':
    base = 'jzgqcdpd'
    hashes: List[Tuple[int, int]] = []
    for i in range(128):
        hash_str: str = '{base}-{index}'.format(base=base, index=str(i))
        inp: List[int] = list(map(ord, hash_str))
        lengths: List[int] = inp + [17, 31, 73, 47, 23]
        dense_hash: List[int] = knot(lengths)

        bin_hash: List[int] = list(bin(
            int(hexdump(dense_hash), 16))[2:].zfill(128))
        hashes.extend([(i, j) for j, k in enumerate(bin_hash) if k == '1'])

    # part 1
    print(len(hashes))
    # part 2
    print(dfs(hashes))
