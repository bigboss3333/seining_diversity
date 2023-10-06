import unittest

from main import simpson_diversity_index


class MyTestCase(unittest.TestCase):
    def test_function_2010(self):
        data = {'species1': 791, 'species2': 174, 'species3': 60,
                'species4': 6, 'species5': 3, 'species6': 2,
                'species7': 2, 'species8': 1}
        val1 = simpson_diversity_index(data)
        self.assertEqual(round(val1,2), 0.39)  # add assertion here

    def test_how_to(self):
        data = {'species1': 13, 'species2': 42, 'species3': 7,
                'species4': 21, 'species5': 17}
        val1 = simpson_diversity_index(data)
        self.assertEqual(round(val1, 2), 0.74)


if __name__ == '__main__':
    unittest.main()
