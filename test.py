import unittest
from p1 import block_length, new_direction
from p2 import get_num, get_index_of, is_in_bounds, get_next_pos, solve_code, KEY_PAD_1, KEY_PAD_2
from p3 import is_valid_triangle


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


if __name__ == '__main__':
    unittest.main()
