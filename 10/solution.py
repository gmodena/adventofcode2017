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

def knot(lst: List[int], lenghts: List[int], rounds: int = 64) -> List[int]:
    cur = 0
    skip = 0
    while rounds > 0:
        lst, cur, skip = myhash(lst, lengths, cur=cur, skip=skip)
        rounds -= 1

    dense_hash = [reduce(xor, lst[i:i+16], 0) for i in range(0, len(lst), 16)]
    return dense_hash

if __name__ == '__main__':
    lst = list(range(256))

    # part 1
    with open('input.txt') as infile:
        lengths: List[int] = list(
            map(int, infile.readline().strip('\n').split(',')))

    sparse_hash, _, _ = myhash(lst, lengths)
    print(sparse_hash[0] * sparse_hash[1])

    # part 2
    with open('input.txt') as infile:
        inp: List[int] = list(map(ord, infile.readline().strip()))
    lengths = inp + [17, 31, 73, 47, 23]
    # xor elements
    dense_hash: List[int] = knot(lst, lengths)
    print(hexdump(dense_hash))

