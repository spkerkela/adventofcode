import unittest
from p1 import block_length, new_direction


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


if __name__ == '__main__':
    unittest.main()
