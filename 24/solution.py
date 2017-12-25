from collections import defaultdict
import operator
def find_bridges(components):
    def dfs(bridge, components):
        # current node
        cur = bridge[-1][1]
        for node in components[cur]:
            if not ((cur, node) in bridge or (node, cur) in bridge):
                new_bridge = bridge + [(cur, node)]
                yield new_bridge
                yield from dfs(new_bridge, components)

    bridges = list(dfs([(0, 0)], components))
    s = []
    for bridge in bridges:
        s.append((len(bridge), sum([x+y for x, y in bridge])))
    return s

def part1(bridges):
    return sorted(bridges, key = operator.itemgetter(1), reverse=True)[0][1]
def part2(bridges):
    return sorted(bridges, key = operator.itemgetter(0, 1), reverse=True)[0][1]

if __name__ == '__main__':
    components = defaultdict(set)
    with open('input.txt') as infile:
        for row in infile.readlines():
            x, y = list(map(int, row.strip().split('/')))
            components[x].add(y)
            components[y].add(x)

    bridges = find_bridges(components)
    print(part1(bridges))
    print(part2(bridges))
