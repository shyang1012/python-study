from sqlite3 import *


class DbConnection(object):
    def __init__(self):
        self.conn = None

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        self.conn = None
        try:
            self.conn = connect(db_file)
        except Error as e:
            print(e)

        return self.conn