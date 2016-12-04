from itertools import permutations


def is_valid_triangle(triangle):
    return all([t[0] + t[1] > t[2] for t in permutations(triangle)])


def create_triangles_from_lines(lines):
    return [(int(line[0]), int(line[1]), int(line[2])) for line in lines]


def create_triangles_from_columns(lines):
    number_of_columns = len(lines[0])
    columns = [[line[n] for line in lines] for n in range(number_of_columns)]
    ret_triangles = []
    for column in columns:
        ts = [column[x:x + 3] for x in range(0, len(column), 3)]
        ret_triangles.extend([(int(t[0]), int(t[1]), int(t[2])) for t in ts])
    return ret_triangles


with open('data/data3.txt', mode='r') as f:
    data = [[s.strip() for s in line.split(' ') if s != ''] for line in f.readlines()]
    triangles = create_triangles_from_lines(data)
    triangles2 = create_triangles_from_columns(data)
    print(len([t for t in triangles if is_valid_triangle(t)]))
    print(len([t for t in triangles2 if is_valid_triangle(t)]))
