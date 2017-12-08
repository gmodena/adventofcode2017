from collections import defaultdict

global tower

def traverse(node):
    yield tower[node]['w']
    for program in tower[node]['programs']:
        yield from traverse(program)

def unbalanced_node(d):
    for k in d:
        if len(d[k]) == 1:
            return d[k][0]

def total_weight(node):
    return sum(list(traverse(node)))

def is_unbalanced(node):
    counter = defaultdict(list)
    for node in tower[node]['programs']:
        counter[total_weight(node)].append(node)
    if len(counter) > 1:
        n = tower[unbalanced_node(counter)]
        weight_diff = abs(list(counter.keys())[0] - list(counter.keys())[1])
        yield n['w'] - weight_diff
        yield from is_unbalanced(unbalanced_node(counter))

def find_unbalanced(node):
    for node in is_unbalanced(root):
        pass
    return node

def get_program(line):
    return line.split(' ')[0]

def get_weight(line):
    return int(line.split(' ')[1].strip('(').strip(')'))

def get_above_program(line):
    return list(map(lambda x: x.strip(' '), line.split(',')))

if __name__ == '__main__':
    tower = {}
    with open('input.txt') as infile:
        for line in infile.readlines():
            line = line.strip('\n')
            weight, program, above_program = None, None, []
            try:
                lhs, rhs = line.split('->')
                program = get_program(lhs)
                weight = get_weight(lhs)
                above_program = get_above_program(rhs)
            except ValueError:
                program = get_program(line)
                weight = get_weight(line)
            finally:
                tower[program] = {'w': weight, 'programs': above_program}

    # Part A
    for root in tower:
        for node in tower:
            if root in tower[node]['programs']:
                break
        else:
            print(root)
            break

    # Part B
    print(find_unbalanced(root))
