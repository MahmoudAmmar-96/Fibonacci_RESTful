
# Imports the PostgreSQL client for Python
import psycopg2

class FibonacciCombinationDatabase:
    def __init__(self, db, username, password):
        self.db = db
        self.username = username
        self.password = password
        self.cur = None
        self.conn = None

    def connect(self):
        # Connect to the database
        try:
            self.con = psycopg2.connect(
                host = "localhost",
                database = self.db,
                user = self.username,
                password = self.password
            )
            print('Database is connected.')
        except:
            print('Database is not connected!')

        self.cursor = self.con.cursor()


    def execute_query(self, query):
        self.cursor.execute(query)
        self.con.commit()


    def close(self):
        self.cursor.close()
        self.con.close()


db = FibonacciCombinationDatabase(db="fibonacci", username="mahmoud", password="lol")
db.connect()
