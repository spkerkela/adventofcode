from copy import deepcopy


def direction_and_length(d):
    return d[0], int(d[1:])


DIRECTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']


def new_direction(cur, l_or_r):
    current_index = DIRECTIONS.index(cur)
    if l_or_r == 'L':
        return DIRECTIONS[current_index - 1]
    elif l_or_r == 'R':
        if current_index + 1 < len(DIRECTIONS):
            return DIRECTIONS[current_index + 1]
        else:
            return DIRECTIONS[0]
    else:
        return cur


def move_towards(cur_pos, direction, blocks):
    ret_pos = deepcopy(cur_pos)
    moved_steps = []
    if direction == DIRECTIONS[0]:
        moved_steps = [{'x': ret_pos['x'], 'y': ret_pos['y'] + n} for n in range(1, blocks + 1)]
        ret_pos['y'] += blocks
    elif direction == DIRECTIONS[1]:
        moved_steps = [{'x': ret_pos['x'] + n, 'y': ret_pos['y']} for n in range(1, blocks + 1)]
        ret_pos['x'] += blocks
    elif direction == DIRECTIONS[2]:
        moved_steps = [{'x': ret_pos['x'], 'y': ret_pos['y'] - n} for n in range(1, blocks + 1)]
        ret_pos['y'] -= blocks
    elif direction == DIRECTIONS[3]:
        moved_steps = [{'x': ret_pos['x'] - n, 'y': ret_pos['y']} for n in range(1, blocks + 1)]
        ret_pos['x'] -= blocks
    return ret_pos, moved_steps


def block_length(directions):
    def blocks_from_origin(p):
        return abs(p['x']) + abs(p['y'])

    path = []
    first_duplicate = None
    walker = {'pos': {'x': 0, 'y': 0},
              'direction': 'NORTH'}
    for d in directions:
        walker['direction'] = new_direction(walker['direction'], d[0])
        walker['pos'], steps = move_towards(walker['pos'], walker['direction'], d[1])
        if not first_duplicate:
            visited = [blocks_from_origin(pp) for p in steps for pp in path if pp['x'] == p['x'] and pp['y'] == p['y']]
            if len(visited) > 0:
                first_duplicate = visited[0]
        path.extend(steps)
    return blocks_from_origin(walker['pos']), first_duplicate


with open('data/data1.txt', mode='r') as f:
    data = [direction_and_length(d.strip()) for d in f.read().strip().split(',')]
    total, first = block_length(data)
    print('Blocks to the HQ: {0}. First location visited twice: {1}.'.format(total, first))
