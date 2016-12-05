import hashlib


def get_password(input_string):
    i = 0
    password = ''
    while len(password) < 8:
        m = hashlib.md5()
        m.update((input_string + str(i)).encode('ascii'))
        hex_digest = m.hexdigest()
        i += 1
        if hex_digest.startswith('00000'):
            password += hex_digest[5]
    return password


def get_password2(input_string):
    i = 0
    password_slots = [None, None, None, None, None, None, None, None]
    while not all(password_slots):
        m = hashlib.md5()
        m.update((input_string + str(i)).encode('ascii'))
        hex_digest = m.hexdigest()
        i += 1
        if hex_digest.startswith('00000') and hex_digest[5].isdigit():
            index_to_insert = int(hex_digest[5])
            if index_to_insert < 8 and password_slots[index_to_insert] is None:
                password_slots[index_to_insert] = hex_digest[6]
    return ''.join(password_slots)


with open('data/data5.txt', mode='r') as f:
    in_str = f.read().strip()
    print(get_password(in_str))
    print(get_password2(in_str))
