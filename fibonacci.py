from flask import Flask
from flask_restful import Resource, Api, abort
from fibonacci_sequence import FibonacciSequence
from combination_sum import CombinationSum

app = Flask(__name__)
api = Api(app)


def abort_if_less_than_two(value):
    if value < 2:
        abort(
            404,
            message="Your input number is {}. Only select a number equals to 2 or more".format(value))


class Fibonacci(Resource):

    def get(self, value):
        abort_if_less_than_two(value)
        fibonacciTerms = FibonacciSequence(value).generated_list
        fibCombinationSum = CombinationSum(
            fibonacciTerms, value).fibonacci_combination
        return {'result': fibCombinationSum}


api.add_resource(Fibonacci, '/fib/<int:value>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
