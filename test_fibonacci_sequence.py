from unittest import TestCase
from fibonacci_sequence import FibonacciSequence


class TestFibonacciSequence(TestCase):
    """
    Testing the FibonacciSequence class
    """

    def test_generate_fibonacci_list_of_0_returns_empty_list(self, value=0):
        fibonacciSequence = FibonacciSequence(value).generated_list
        self.assertEqual(len(fibonacciSequence), value)
        self.assertEqual(fibonacciSequence, [])


    def test_generate_fibonacci_list_of_30_returns_correct_list(self, value=30):
        fibonacciSequence = FibonacciSequence(value).generated_list
        self.assertEqual(len(fibonacciSequence), 6)
        self.assertEqual(fibonacciSequence, [2, 3, 5, 8, 13, 21])


    def test_generate_fibonacci_list_of_2000_returns_correct_list(self, value=2000):
        fibonacciSequence = FibonacciSequence(value).generated_list
        self.assertEqual(len(fibonacciSequence), 15)
        self.assertEqual(fibonacciSequence, [
            2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
        ])