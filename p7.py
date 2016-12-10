import re
from itertools import islice

regex = "(\[(?:\[??[^\[]*?\]))"

prog = re.compile(regex)


def window(seq, n=2):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def is_abba(in_str):
    return len(set(in_str)) == 2 and in_str == in_str[::-1]


def is_aba(in_str):
    return len(set(in_str)) == 2 and in_str[0] == in_str[-1]


def get_hyper_nets(in_str):
    res = prog.findall(in_str)
    return [r[1:-1] for r in res]


def get_non_hyper(in_str):
    return prog.sub('', in_str)


def compare_aba_pair(left, right):
    return left[0] == right[1] and left[1] == right[0]


def supports_ssl(in_str):
    hyper_nets = get_hyper_nets(in_str)
    non_hyper = get_non_hyper(in_str)
    sliced = sliced_to_n(non_hyper, 3)
    nets_sliced = [sliced_to_n(s, 3) for s in hyper_nets]
    for net in nets_sliced:
        for n in net:
            if is_aba(n):
                for sl in sliced:
                    if is_aba(sl) and compare_aba_pair(n, sl):
                        return True
    return False


def supports_tls(in_str):
    hyper_nets = get_hyper_nets(in_str)
    non_hyper = get_non_hyper(in_str)
    sliced = sliced_to_n(non_hyper, 4)
    nets_sliced = [sliced_to_n(s, 4) for s in hyper_nets]
    any_is_abba = any([is_abba(s) for s in sliced])
    any_in_hyper_is_abba = any([any([is_abba(s) for s in slices]) for slices in nets_sliced])
    return any_is_abba and not any_in_hyper_is_abba


def sliced_to_n(in_str, n):
    sliced = [''.join(w) for w in window(in_str, n)]
    return sliced


def how_many_support_tls():
    with open('data/data7.txt', mode='r') as f:
        data = [line.strip() for line in f.readlines()]
        print(len([f for f in data if supports_tls(f)]))
        print(len([f for f in data if supports_ssl(f)]))


if __name__ == '__main__':
    how_many_support_tls()
