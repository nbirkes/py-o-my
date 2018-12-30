import unittest
import phonie


class TestPhonie(unittest.TestCase):

    def test_2(self):
        expected = ['A', 'B', 'C']
        actual = phonie.build_possibilities('2', [])
        self.assertEqual(expected, actual)

    def test_8_2(self):
        expected = [
            'A',
            'B',
            'C',
            'TA',
            'UA',
            'VA',
            'TB',
            'UB',
            'VB',
            'TC',
            'UC',
            'VC',
        ]
        actual = phonie.build_possibilities('2', [])
        actual = phonie.build_possibilities('8', actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
