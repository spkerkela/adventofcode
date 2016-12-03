from itertools import permutations


def is_valid_triangle(triangle):
    return all([t[0] + t[1] > t[2] for t in permutations(triangle)])


def create_triangles(lines):
    return [(int(line[0]), int(line[1]), int(line[2])) for line in lines]


with open('data/data3.txt', mode='r') as f:
    triangles = create_triangles([[s.strip() for s in line.split(' ') if s != ''] for line in f.readlines()])
    print(len([t for t in triangles if is_valid_triangle(t)]))
