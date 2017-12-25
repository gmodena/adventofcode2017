def dfs(graph, visited=[]):
    if len(visited) == 1:
        yield visited[0]
    cur = visited[-1]
    for node in graph[cur]:
        if not node in visited:
            visited.append(node)
            yield node
            yield from dfs(graph, visited)

def part1(graph):
    start = [0]
    group = list(dfs(graph, start))
    return len(group)

def part2(graph):
    connected_nodes = set()
    connected_components = 0
    for node in graph.keys():
        if node not in connected_nodes:
            group = sorted(list(dfs(graph, [node])))
            connected_nodes.update(group)
            connected_components += 1
    return(connected_components)


if __name__ == '__main__':
    graph = {}
    with open('input.txt') as infile:
        for line in infile.readlines():
            lhs, rhs = line.strip('\n').split('<->')
            graph[int(lhs.strip(' '))] = set([int(x.strip(' '))
                                          for x in rhs.split(',')])

    print(part1(graph))
    print(part2(graph))
