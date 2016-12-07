def get_char(line, reversed):
    counted = [(c, line.count(c)) for c in line]
    counted.sort(key=lambda k: k[1], reverse=reversed)
    return counted[0][0]


def get_most_common_char(line):
    return get_char(line, True)


def get_least_common_char(line):
    return get_char(line, False)


def get_error_corrected(messages):
    columns = [[m[n] for m in messages] for n in range(len(messages[0]))]

    columns_joined = [''.join(c) for c in columns]
    common_chars = [get_most_common_char(cc) for cc in columns_joined]
    least_common_chars = [get_least_common_char(cc) for cc in columns_joined]
    return ''.join(common_chars), ''.join(least_common_chars)


def get_encrypted_password():
    with open('data/data6.txt', mode='r') as f:
        data = [line.strip() for line in f.readlines()]
        print(get_error_corrected(data))


if __name__ == '__main__':
    get_encrypted_password()
