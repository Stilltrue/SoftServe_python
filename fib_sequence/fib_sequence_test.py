import unittest
import sys
import subprocess

from fib_sequence_2 import FibonacciSequence


class TestClassEnvelopeAnalysis(unittest.TestCase):

    def test_wrong_number_type_error(self):
        self.assertRaises(TypeError, lambda: FibonacciSequence("str", True))
        self.assertRaises(TypeError, lambda: FibonacciSequence(9, "abc"))
        self.assertRaises(TypeError, lambda: FibonacciSequence(True, 5))
        self.assertRaises(TypeError, lambda: FibonacciSequence(False, 7.1))
        self.assertRaises(TypeError, lambda: FibonacciSequence(5, True))
        self.assertRaises(TypeError, lambda: FibonacciSequence(9.3, "bc"))
        self.assertRaises(TypeError, lambda: FibonacciSequence("qbc", 9.9))
        self.assertRaises(TypeError, lambda: FibonacciSequence(7, 8.1))
        self.assertRaises(TypeError, lambda: FibonacciSequence(5.0, 6))
        self.assertRaises(TypeError, lambda: FibonacciSequence(5, 5.0))

    def test_incorrect_value_sides_error(self):
        self.assertRaises(ValueError, lambda: FibonacciSequence(7, -2))
        self.assertRaises(ValueError, lambda: FibonacciSequence(-7, 6))
        self.assertRaises(ValueError, lambda: FibonacciSequence(-8, -7))


if __name__ == '__main__':
    unittest.main()
    if '--unittest' in sys.argv:
        subprocess.call([sys.executable, '-m', 'unittest', 'discover'])