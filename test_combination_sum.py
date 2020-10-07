from unittest import TestCase
from fibonacci_sequence import FibonacciSequence
from combination_sum import CombinationSum


class TestCombinationSum(TestCase):
    """
    Testing the CombinationSum class
    """

    def test_generate_fibonacci_list_of_0_returns_empty_list(self, value=0):
        fibonacciSequence = FibonacciSequence(value).generated_list
        fibonacciCombination = CombinationSum(fibonacciSequence, value).fibonacci_combination
        self.assertEqual(len(fibonacciCombination[0]), 0)
        self.assertEqual(fibonacciCombination[0], [])


    def test_generate_fibonacci_list_of_4_returns_correct_combination(self, value=4):
        fibonacciSequence = FibonacciSequence(value).generated_list
        fibonacciCombination = CombinationSum(fibonacciSequence, value).fibonacci_combination
        self.assertEqual(len(fibonacciCombination), 1)
        self.assertEqual(fibonacciCombination[0], [2,2])


    def test_generate_fibonacci_list_of_11_returns_correct_combination(self, value=11):
        fibonacciSequence = FibonacciSequence(value).generated_list
        fibonacciCombination = CombinationSum(fibonacciSequence, value).fibonacci_combination
        self.assertEqual(len(fibonacciCombination), 5)
        self.assertEqual(fibonacciCombination[0], [3, 8])
        self.assertEqual(fibonacciCombination[1], [2, 2, 2, 2, 3])
        self.assertEqual(fibonacciCombination[2], [2, 2, 2, 5])
        self.assertEqual(fibonacciCombination[3], [2, 3, 3, 3])
        self.assertEqual(fibonacciCombination[4], [3, 3, 5])
