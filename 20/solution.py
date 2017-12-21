from itertools import combinations
from copy import deepcopy

def update(particle):
    particle['v'][0] += particle['a'][0]
    particle['v'][1] += particle['a'][1]
    particle['v'][2] += particle['a'][2]

    particle['p'][0] += particle['v'][0]
    particle['p'][1] += particle['v'][1]
    particle['p'][2] += particle['v'][2]
    return particle

def distance(particle):
    return sum([abs(x) for x in particle['p']])

def part1(particles):
    closest = 0
    for time in range(1000):
        distances = []
        for index, particle in enumerate(particles):
            particle = update(particle)
            distances.append(distance(particle))

        minidx = min(distances)
        closest = distances.index(minidx)
    return closest

def part2(particles):
    for time in range(100):
        colliding = []
        particles = [update(particle) for particle in particles]
        for combi in combinations(particles, 2):
            if combi[0]['p'] == combi[1]['p']:
                colliding.append(combi[0])
                colliding.append(combi[1])
        for col in colliding:
            if col in particles:
                particles.remove(col)
    return len(particles)

if __name__ == '__main__':
    particles = []
    with open('input.txt') as infile:
        for line in infile:
            line = line.strip().split(", ")
            p = [int(x) for x in line[0].split("=")[1][1:-1].split(",")]
            v = [int(x) for x in line[1].split("=")[1][1:-1].split(",")]
            a = [int(x) for x in line[2].split("=")[1][1:-1].split(",")]
            particles.append({'p': p, 'v': v, 'a': a })

    print(part1(deepcopy(particles)))
    print(part2(deepcopy(particles)))
