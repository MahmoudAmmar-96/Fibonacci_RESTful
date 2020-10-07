

class FibonacciSequence:
    """
    class FibonacciSequence to generate a fibonacci
    sequence for a specific number

    Parameters
    ----------
    value : int
        the number to be used to generate the fibonacci sequence

    Attributes
    ----------
    generated_list : list
        the generated fibonacci sequence
    """

    def __init__(self, value):
        self.value = value
        self.fibonacciTerms = []
        self.generate_fibonacci_list()

    def generate_fibonacci_list(self, index=2):
        """
        generates the list that contains the fibonacci sequence

        Parameters
        ----------
        index : int
            used for indexing to reuse the last two generated terms
            of the fibonacci list
        """
        self.fibonacciTerms.append(1)
        self.fibonacciTerms.append(1)

        # Add to the list all the Fibonacci terms for the input value
        while True:
            newFibonacciTerm = (
                self.fibonacciTerms[index - 1] + self.fibonacciTerms[index - 2])

            # Leave the loop when the required sequence is calculated
            if newFibonacciTerm > self.value:
                break

            self.fibonacciTerms.append(newFibonacciTerm)
            index += 1

    @property
    def generated_list(self):
        return self.fibonacciTerms[2:]
