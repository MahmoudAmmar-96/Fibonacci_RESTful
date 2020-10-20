
import sqlite3


class FibonacciCombinationDatabase:
    """
    class FibonacciCombinationDatabase to add calculated
    combinations to the database

    Attributes
    ----------
    get_combination : list[list]
        the generated combinations sums of the fibonacci 
        sequence which are saved in the database.
    """

    def __init__(self):
        self.conn = sqlite3.connect('combinations.db')
        self.cur = self.conn.cursor()

        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS Combinations (number INTEGER, combination STRING)''')

    def execute(self, query, data):
        self.cur.execute(query, data)
        self.conn.commit()

    def add_combination(self, number, combination):
        """
        adds the number and its calculated combination 
        into the database table

        Parameters
        ----------
        number : int
            the number used to to find the combination sums
        combination : int
            the list containing the combination sum
        """

        self.execute(
            '''INSERT INTO Combinations (number, combination) VALUES (?,?)''', (number, combination))

    def get_combination(self, num):
        """
        gets the generated combination of variable number from
        the database table. Returns None if it doesn't exist

        Parameters
        ----------
        num : int
            the number used to to find the combination sums
        """

        self.execute(
            '''SELECT combination FROM Combinations WHERE number = ? ''', (num,))
        return self.cur.fetchone()

    def __del__(self):
        """
        Destroys instance and connection on completion of called method 
        """
        self.conn.close()
