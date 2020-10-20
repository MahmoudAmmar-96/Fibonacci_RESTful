from flask import Flask
from flask_restful import Resource, Api, abort
from fibonacci_sequence import FibonacciSequence
from combination_sum import CombinationSum
from fibonacci_combination_database import FibonacciCombinationDatabase

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
        db = FibonacciCombinationDatabase()

        # Check if the combination of the value is already calculated and saved in the database
        if db.get_combination(value) is None:
            fibonacciTerms = FibonacciSequence(value).generated_list
            fibCombinationSum = CombinationSum(
                fibonacciTerms, value).fibonacci_combination
            db.add_combination(value, str([fibCombinationSum]))
        else:
            fibCombinationSum = db.get_combination(value)

        return {'result': fibCombinationSum}


api.add_resource(Fibonacci, '/fib/<int:value>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
