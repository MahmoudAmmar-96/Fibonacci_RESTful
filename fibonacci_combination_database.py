
import sqlite3


class FibonacciCombinationDatabase:

    def __init__(self):
        self.conn = sqlite3.connect('combinations.db')
        self.cur = self.conn.cursor()

        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS Combinations (number INTEGER, combination STRING)''')

    def execute(self, query, data):
        self.cur.execute(query, data)
        self.conn.commit()

    def add_combination(self, number, combination):
        self.execute(
            '''INSERT INTO Combinations (number, combination) VALUES (?,?)''', (number, combination))

    def check_number(self, num):
        self.execute(
            '''SELECT combination FROM Combinations WHERE number = ? ''', (num,))
        return self.cur.fetchone()

    def __del__(self):
        """ Destroys instance and connection on completion of called method """
        self.conn.close()
