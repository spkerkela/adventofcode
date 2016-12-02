KEY_PAD_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

KEY_PAD_2 = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None]
]

DIRECTIONS = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}


def get_index_of(start_from, key_pad):
    for yi, y in enumerate(key_pad):
        for xi, x in enumerate(key_pad[yi]):
            if start_from == x:
                return xi, yi


def is_in_bounds(pos, key_pad):
    x, y = pos
    return 0 <= y < len(key_pad) and 0 <= x < len(key_pad[y]) and key_pad[y][x] is not None


def get_next_pos(pos, direction, key_pad):
    x, y = pos
    new_dir = DIRECTIONS[direction]
    x2, y2 = new_dir
    new_pos = (x + x2, y + y2)
    if is_in_bounds(new_pos, key_pad):
        return new_pos
    else:
        return pos


def get_num(start_from, directions, key_pad):
    pos = get_index_of(start_from, key_pad)
    for d in directions:
        pos = get_next_pos(pos, d, key_pad)
    x, y = pos
    return key_pad[y][x]


def solve_code(code_lines, key_pad):
    start_from = 5
    code = []
    for line in code_lines:
        start_from = get_num(start_from, list(line), key_pad)
        code.append(str(start_from))
    return ''.join(code)


with open('data/data2.txt', mode='r') as f:
    lines = [line.strip() for line in f.readlines()]
    print(solve_code(lines, KEY_PAD_1))
    print(solve_code(lines, KEY_PAD_2))
