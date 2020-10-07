from unittest import TestCase
from flask import json
from fibonacci import app


class TestFibonacci(TestCase):
    """
    Testing the Fibonacci class
    """

    def setUp(self):
        self.client = app.test_client()


    def test_value_returns_404(self):
        response = self.client.get('/fib/1')
        self.assertEqual(response.status_code, 404)


    def test_value_less_tha_two_returns_correct_error_message(self):
        response = self.client.get('/fib/1')
        error_message = self._get_error_message(response)
        self.assertEqual('Your input number is 1. Only select a number equals to 2 or more'
                         , error_message)


    def test_wrong_path_returns_404(self):
        response = self.client.get('fib/wrongpath/1223')
        self.assertEqual(response.status_code, 404)


    def test_size_is_2_returns_200(self):
        response = self.client.get('fib/2')
        self.assertEqual(response.status_code, 200)


    def test_size_is_8_returns_200_with_correct_list(self):
        response = self.client.get('fib/8')
        response_data = json.loads(response.data)
        fibonacci_list = response_data.get("result")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(fibonacci_list[0], [8])
        self.assertEqual(fibonacci_list[1], [2,2,2,2])
        self.assertEqual(fibonacci_list[2], [2,3,3])
        self.assertEqual(fibonacci_list[3], [3,5])


    def _get_error_message(self, response):
        response_data = json.loads(response.data)
        error_message = response_data.get("message")
        return error_message