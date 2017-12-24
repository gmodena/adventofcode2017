from collections import defaultdict
import operator

def dfs(bridge, components):
    # current node
    cur = bridge[-1][1]
    for node in components[cur]:
        if (cur, node) not in bridge and (node, cur) not in bridge:
            new_bridge = bridge + [(cur, node)]
            yield new_bridge
            yield from dfs(new_bridge, components)

def part1(bridges):
    s = []
    for bridge in bridges:
        s.append(sum([x+y for x, y in bridge]))
    return max(s)

def part2(bridges):
    s = []
    for bridge in bridges:
        s.append((len(bridge), sum([x+y for x, y in bridge])))
    return sorted(s, key = operator.itemgetter(0, 1), reverse=True)[0]

if __name__ == '__main__':
    components = defaultdict(set)


    with open('input.txt') as infile:
        for row in infile.readlines():
            row = list(map(int, row.strip().split('/')))
            components[row[0]].add(row[1])
            components[row[1]].add(row[0])
    bridges = list(dfs([(0, 0)], components))
    print(part2(bridges))
