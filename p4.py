import string, itertools


def get_checksum(data):
    return data[data.index('[') + 1:data.index(']')]


def get_room_id(data):
    return int(data[data.rindex('-') + 1:data.index('[')])


def compile_checksum(data):
    code = get_code(data)
    chars_in_code = {c for c in code if c in string.ascii_letters}
    occurences = [(c, data.count(c)) for c in chars_in_code]
    occurences.sort(key=lambda k: k[0], reverse=False)
    occurences.sort(key=lambda k: k[1], reverse=True)
    compiled_sum = ''.join([c[0] for c in occurences[:5]])
    return compiled_sum


def get_code(data):
    return data[:data.rindex('-')]


def is_real_room(room_str):
    return get_checksum(room_str) == compile_checksum(room_str)


def get_sum_of_codes(lines):
    return sum([get_room_id(line) for line in lines if is_real_room(line)])


def decrypt_name(encrypted, room_id):
    ret = ''
    for c in encrypted:
        if c == '-':
            ret += ' '
        else:
            ascii_lookup = itertools.cycle(string.ascii_lowercase)
            index = string.ascii_lowercase.index(c)
            temp = [s for s in itertools.islice(ascii_lookup, index, index + room_id + 1)]
            ret += temp[-1]
    return ret


def real_name_and_code(room_str):
    code = get_code(room_str)
    room_id = get_room_id(room_str)
    return decrypt_name(code, room_id), room_id


with open('data/data4.txt', mode='r') as f:
    lines = list(f.readlines())
    names = [real_name_and_code(line) for line in lines if is_real_room(line)]
    north_pole = [name for name in names if (name[0] == 'northpole object storage')]
    print(north_pole)
    print(get_sum_of_codes(lines))
