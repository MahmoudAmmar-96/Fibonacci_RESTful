

class CombinationSum:
    """
    class CombinationSum to generate the list of all possible
    combination sums of the generated fibonacci sequence

    Parameters
    ----------
    fibonacciTerms : list[int]
        the generated fibonacci sequence
    value : int
        the number used to generate the fibonacci sequence

    Attributes
    ----------
    fibonacci_combination : list[list]
        the generated combinations sums of the fibonacci sequence
    """

    def __init__(self, fibonacciTerms, value):
        self.fibonacciTerms = list(set(fibonacciTerms))
        self.fibonacciCombinationSum = []
        self.unique = {}
        self.solve(value)

    def solve(self, value, i=0, current=[]):
        """
        finds all the possible combination sums of the generated
        fibonacci sequence in a recursive manner using Combination
        Sum algorithm

        reference: https://www.tutorialspoint.com/combination-sum-in-python

        Parameters
        ----------
        value : int
            the number used to to find the combination sums
        """
        if value == 0:
            temp = [i for i in current]
            temp1 = temp
            temp.sort()
            temp = tuple(temp)

            # Checks if the temporary sorted list is unique and if so append it
            # to the main combination sum list
            if temp not in self.unique:
                self.unique[temp] = 1
                self.fibonacciCombinationSum.append(temp1)
            pass
        elif value < 0:
            return
        else:
            pass

        for x in range(i, len(self.fibonacciTerms)):
            current.append(self.fibonacciTerms[x])
            self.solve(value - self.fibonacciTerms[x], i, current)
            current.pop(len(current) - 1)

    @property
    def fibonacci_combination(self):
        return self.fibonacciCombinationSum
