import unittest

from challenges.sort import bubble_sort
from challenges.challenges import radians_to_degrees


class TestChallenges(unittest.TestCase):
    def test_radians(self):
        expected = 360
        output = radians_to_degrees(6.283185307179586)
        self.assertEqual(expected, output)

        expected = 180
        output = radians_to_degrees(3.141592653589793)
        self.assertEqual(expected, output)

        expected = 90
        output = radians_to_degrees(1.5707963267948966)
        self.assertEqual(expected, output)

    def test_sort_list(self):
        expected = [1, 2, 3, 4, 5]
        output = bubble_sort([5, 3, 1, 2, 4])
        self.assertEqual(expected, output)

        expected = [1, 2, 3, 4, 5]
        output = bubble_sort([1, 2, 3, 4, 5])
        self.assertEqual(expected, output)

        expected = [1, 2, 3, 4, 5]
        output = bubble_sort([5, 4, 3, 2, 1])
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
