import unittest
from p1 import block_length, new_direction
from p2 import get_num, get_index_of, is_in_bounds, get_next_pos, solve_code, KEY_PAD_1, KEY_PAD_2
from p3 import is_valid_triangle
from p4 import is_real_room, get_checksum, get_code, get_room_id, get_sum_of_codes, decrypt_name
from p5 import get_password, get_password2
from p6 import get_error_corrected
from p7 import supports_tls, is_abba, get_hyper_nets, sliced_to_n, supports_ssl, is_aba, compare_aba_pair
from p8 import create_screen, rotate_screen


class TestP1(unittest.TestCase):
    def test_block_length(self):
        self.assertEqual(block_length([('R', 2), ('L', 3)]), (5, None))
        self.assertEqual(block_length([('R', 2), ('R', 2), ('R', 2)]), (2, None))
        self.assertEqual(block_length([('R', 5), ('L', 5), ('R', 5), ('R', 3)]), (12, None))
        self.assertEqual(block_length([('R', 8), ('R', 4), ('R', 4), ('R', 8)]), (8, 4))

    def test_new_direction(self):
        self.assertEqual(new_direction('NORTH', 'R'), 'EAST')
        self.assertEqual(new_direction('EAST', 'R'), 'SOUTH')
        self.assertEqual(new_direction('SOUTH', 'R'), 'WEST')
        self.assertEqual(new_direction('WEST', 'R'), 'NORTH')
        self.assertEqual(new_direction('NORTH', 'L'), 'WEST')
        self.assertEqual(new_direction('EAST', 'L'), 'NORTH')
        self.assertEqual(new_direction('SOUTH', 'L'), 'EAST')
        self.assertEqual(new_direction('WEST', 'L'), 'SOUTH')


class TestP2(unittest.TestCase):
    def test_solve_(self):
        self.assertEqual(solve_code(['ULL', 'RRDDD', 'LURDL', 'UUUUD'], KEY_PAD_1), '1985')
        self.assertEqual(solve_code(['ULL', 'RRDDD', 'LURDL', 'UUUUD'], KEY_PAD_2), '5DB3')

    def test_get_index_of(self):
        self.assertEqual(get_index_of(1, KEY_PAD_1), (0, 0))
        self.assertEqual(get_index_of(2, KEY_PAD_1), (1, 0))
        self.assertEqual(get_index_of(3, KEY_PAD_1), (2, 0))
        self.assertEqual(get_index_of(4, KEY_PAD_1), (0, 1))
        self.assertEqual(get_index_of(5, KEY_PAD_1), (1, 1))
        self.assertEqual(get_index_of(6, KEY_PAD_1), (2, 1))
        self.assertEqual(get_index_of(7, KEY_PAD_1), (0, 2))
        self.assertEqual(get_index_of(8, KEY_PAD_1), (1, 2))
        self.assertEqual(get_index_of(9, KEY_PAD_1), (2, 2))
        self.assertEqual(get_index_of(1, KEY_PAD_2), (2, 0))
        self.assertEqual(get_index_of(2, KEY_PAD_2), (1, 1))
        self.assertEqual(get_index_of(3, KEY_PAD_2), (2, 1))
        self.assertEqual(get_index_of(4, KEY_PAD_2), (3, 1))
        self.assertEqual(get_index_of(5, KEY_PAD_2), (0, 2))
        self.assertEqual(get_index_of(6, KEY_PAD_2), (1, 2))
        self.assertEqual(get_index_of(7, KEY_PAD_2), (2, 2))
        self.assertEqual(get_index_of(8, KEY_PAD_2), (3, 2))
        self.assertEqual(get_index_of(9, KEY_PAD_2), (4, 2))
        self.assertEqual(get_index_of('A', KEY_PAD_2), (1, 3))
        self.assertEqual(get_index_of('B', KEY_PAD_2), (2, 3))
        self.assertEqual(get_index_of('C', KEY_PAD_2), (3, 3))
        self.assertEqual(get_index_of('D', KEY_PAD_2), (2, 4))

    def test_get_num(self):
        self.assertEqual(get_num(5, ['U', 'L', 'L'], KEY_PAD_1), 1)
        self.assertEqual(get_num(5, ['R', 'R', 'D', 'D', 'D'], KEY_PAD_1), 9)
        self.assertEqual(get_num(9, ['L', 'U', 'R', 'D', 'L'], KEY_PAD_1), 8)
        self.assertEqual(get_num(8, ['U', 'U', 'U', 'U', 'D'], KEY_PAD_1), 5)
        self.assertEqual(get_num(5, ['U', 'L', 'L'], KEY_PAD_2), 5)
        self.assertEqual(get_num(5, ['R', 'R', 'D', 'D', 'D'], KEY_PAD_2), 'D')
        self.assertEqual(get_num('D', ['L', 'U', 'R', 'D', 'L'], KEY_PAD_2), 'B')
        self.assertEqual(get_num('B', ['U', 'U', 'U', 'U', 'D'], KEY_PAD_2), 3)

    def test_bounds(self):
        self.assertTrue(is_in_bounds((0, 0), KEY_PAD_1))
        self.assertTrue(is_in_bounds((2, 0), KEY_PAD_1))
        self.assertTrue(is_in_bounds((0, 2), KEY_PAD_1))
        self.assertTrue(is_in_bounds((2, 2), KEY_PAD_1))
        self.assertFalse(is_in_bounds((-1, 0), KEY_PAD_1))
        self.assertFalse(is_in_bounds((0, -1), KEY_PAD_1))
        self.assertFalse(is_in_bounds((3, 0), KEY_PAD_1))
        self.assertFalse(is_in_bounds((0, 3), KEY_PAD_1))

    def test_get_next_pos(self):
        self.assertEqual(get_next_pos((0, 0), 'U', KEY_PAD_1), (0, 0))
        self.assertEqual(get_next_pos((1, 1), 'U', KEY_PAD_1), (1, 0))
        self.assertEqual(get_next_pos((1, 1), 'D', KEY_PAD_1), (1, 2))
        self.assertEqual(get_next_pos((2, 2), 'D', KEY_PAD_1), (2, 2))
        self.assertEqual(get_next_pos((0, 0), 'L', KEY_PAD_1), (0, 0))
        self.assertEqual(get_next_pos((2, 0), 'L', KEY_PAD_1), (1, 0))
        self.assertEqual(get_next_pos((2, 0), 'R', KEY_PAD_1), (2, 0))
        self.assertEqual(get_next_pos((1, 0), 'R', KEY_PAD_1), (2, 0))
        self.assertEqual(get_next_pos((2, 0), 'U', KEY_PAD_2), (2, 0))
        self.assertEqual(get_next_pos((2, 0), 'D', KEY_PAD_2), (2, 1))
        self.assertEqual(get_next_pos((2, 1), 'D', KEY_PAD_2), (2, 2))
        self.assertEqual(get_next_pos((2, 2), 'D', KEY_PAD_2), (2, 3))
        self.assertEqual(get_next_pos((2, 3), 'D', KEY_PAD_2), (2, 4))


class TestP3(unittest.TestCase):
    def test_is_valid_triangle(self):
        self.assertFalse(is_valid_triangle((5, 10, 25)))


class TestP4(unittest.TestCase):
    def test_is_real_room(self):
        self.assertTrue(is_real_room('aaaaa-bbb-z-y-x-123[abxyz]'))
        self.assertTrue(is_real_room('a-b-c-d-e-f-g-h-987[abcde]'))
        self.assertTrue(is_real_room('not-a-real-room-404[oarel]'))
        self.assertFalse(is_real_room('totally-real-room-200[decoy]'))

    def test_get_checksum(self):
        self.assertEqual(get_checksum('aaaaa-bbb-z-y-x-123[abxyz]'), 'abxyz')
        self.assertEqual(get_checksum('a-b-c-d-e-f-g-h-987[abcde]'), 'abcde')
        self.assertEqual(get_checksum('not-a-real-room-404[oarel]'), 'oarel')
        self.assertEqual(get_checksum('totally-real-room-200[decoy]'), 'decoy')

    def test_get_code(self):
        self.assertEqual(get_code('aaaaa-bbb-z-y-x-123[abxyz]'), 'aaaaa-bbb-z-y-x')
        self.assertEqual(get_code('a-b-c-d-e-f-g-h-987[abcde]'), 'a-b-c-d-e-f-g-h')
        self.assertEqual(get_code('not-a-real-room-404[oarel]'), 'not-a-real-room')
        self.assertEqual(get_code('totally-real-room-200[decoy]'), 'totally-real-room')

    def test_get_room_id(self):
        self.assertEqual(get_room_id('aaaaa-bbb-z-y-x-123[abxyz]'), 123)
        self.assertEqual(get_room_id('a-b-c-d-e-f-g-h-987[abcde]'), 987)
        self.assertEqual(get_room_id('not-a-real-room-404[oarel]'), 404)
        self.assertEqual(get_room_id('totally-real-room-200[decoy]'), 200)

    def test_sum_of_codes(self):
        self.assertEqual(get_sum_of_codes(['aaaaa-bbb-z-y-x-123[abxyz]',
                                           'a-b-c-d-e-f-g-h-987[abcde]',
                                           'not-a-real-room-404[oarel]',
                                           'totally-real-room-200[decoy]']), 1514)

    def test_decrypt_name(self):
        self.assertEqual(decrypt_name('qzmt-zixmtkozy-ivhz', 343), 'very encrypted name')


class TestP5(unittest.TestCase):
    def test_get_password(self):
        # self.assertEqual('18f47a30', get_password('abc'))
        # self.assertEqual('05ace8e3', get_password2('abc'))
        pass


class TestP6(unittest.TestCase):
    def test_error_corrected(self):
        messages = [
            'eedadn',
            'drvtee',
            'eandsr',
            'raavrd',
            'atevrs',
            'tsrnev',
            'sdttsa',
            'rasrtv',
            'nssdts',
            'ntnada',
            'svetve',
            'tesnvt',
            'vntsnd',
            'vrdear',
            'dvrsen',
            'enarar'
        ]
        self.assertEqual(('easter', 'advent'), get_error_corrected(messages))


class TestP7(unittest.TestCase):
    def test_slicer(self):
        self.assertEqual(['abcd', 'bcde'], sliced_to_n('abcde', 4))
        self.assertEqual(['abc', 'bcd', 'cde'], sliced_to_n('abcde', 3))

    def test_get_hyper_nets(self):
        self.assertEqual(['abcd', 'efgh'], get_hyper_nets('lolblal[abcd]derpdorp[efgh]'))
        self.assertEqual(['abcd'], get_hyper_nets('lolblal[abcd]derpdorpefgh'))

    def test_is_abba(self):
        self.assertTrue(is_abba('abba'))
        self.assertTrue(is_abba('baab'))
        self.assertTrue(is_abba('xyyx'))
        self.assertFalse(is_abba('yyyx'))
        self.assertFalse(is_abba('xyyy'))
        self.assertFalse(is_abba('yyyy'))

    def test_is_aba(self):
        self.assertTrue(is_aba('aba'))
        self.assertTrue(is_aba('bab'))
        self.assertTrue(is_aba('xox'))
        self.assertFalse(is_aba('xoy'))
        self.assertFalse(is_aba('xxx'))

    def test_supports_tls(self):
        self.assertTrue(supports_tls('abba[mnop]qrst'))
        self.assertFalse(supports_tls('aaaa[mnop]qrst'))
        self.assertTrue(supports_tls('iabba[mnop]qrstt'))
        self.assertFalse(supports_tls('abcd[bddb]xyyx'))
        self.assertFalse(supports_tls('abcd[bddb]aixyyx'))
        self.assertFalse(supports_tls('abcd[abddbc]xyyx'))
        self.assertFalse(supports_tls('abcd[abddbb]xyyx'))
        self.assertFalse(supports_tls('abcd[abddbb]aaaa'))
        self.assertTrue(supports_tls('ioxxoj[asdfgh]zxcvbn'))

    def test_supports_ssl(self):
        self.assertTrue(supports_ssl('aba[bab]xyz'))
        self.assertTrue(supports_ssl('aaa[kek]eke'))
        self.assertTrue(supports_ssl('zazbz[bzb]cdb'))
        self.assertFalse(supports_ssl('xyx[xyx]xyx'))

    def test_aba_pair(self):
        self.assertTrue(compare_aba_pair('aba', 'bab'))
        self.assertTrue(compare_aba_pair('bab', 'aba'))
        self.assertFalse(compare_aba_pair('xab', 'xba'))
        self.assertFalse(compare_aba_pair('xax', 'xax'))


class TestP8(unittest.TestCase):
    def test_create_screen(self):
        self.assertEqual([['.', '.'],
                          ['.', '.'],
                          ['.', '.']], create_screen(2, 3))

    def test_rotate_screen(self):
        screen = [['#', '#', '#', '.', '.', '.', '.'],
                  ['#', '#', '#', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.']]

        self.assertEqual([['#', '.', '#', '.', '.', '.', '.'],
                          ['#', '#', '#', '.', '.', '.', '.'],
                          ['.', '#', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.']], rotate_screen(screen,
                                                                              {'axis': 'row',
                                                                               'index': 1,
                                                                               'amount': 1}))


if __name__ == '__main__':
    unittest.main()
