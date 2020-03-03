"""
This file demonstrates common uses for the Python unittest module
https://docs.python.org/3/library/unittest.html
"""
import sys
from io import StringIO
import textwrap
import unittest


# import backend-modules-packages-assessment.numseq as ns
# import numseq
__author__ = 'Derek Barnes w/ assistance of Piero'


class Capturing(list):
    """Context Mgr helper for capturing stdout from a function call"""
    ''' This is the code of: Piero Madar '''
    # Capturing 'returns' a list of whatever is written
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


class TestNumSeqFunctions(unittest.TestCase):
    """ This is one of potentially many TestCases """

    def test_fib(self):
        from numseq.fib import fib
        expected_fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        actual_fibs = [fib(i) for i in range(10)]
        self.assertListEqual(actual_fibs, expected_fibs)

    def test_square(self):
        pass

    def test_triangle(self):
        pass

    def test_cube(self):
        pass

    def test_geometric_numbers(self):
        from numseq.geo import square, triangle, cube

        with Capturing() as output:
            for i in range(10):
                print('{}: {} {} {}'.format(
                    i, square(i), triangle(i), cube(i)))

        expected_output = textwrap.dedent(
            """\
            0: 0 0 0
            1: 1 1 1
            2: 4 3 8
            3: 9 6 27
            4: 16 10 64
            5: 25 15 125
            6: 36 21 216
            7: 49 28 343
            8: 64 36 512
            9: 81 45 729"""
            ).split('\n')

        self.assertListEqual(output, expected_output)

    def test_is_prime(self):
        from numseq.prime import is_prime
        self.assertTrue(is_prime(7))

    def test_primes(self):
        from numseq.prime import primes
        self.assertEqual(len(primes(5)), 3)
        self.assertEqual(primes(1000)[-1], 997)


if __name__ == '__main__':
    unittest.main()
