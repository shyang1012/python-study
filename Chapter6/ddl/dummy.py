import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def insert_dummy_data(conn,data):
    sql = ''' INSERT INTO BBS(  bid ,
                                writer ,
                                subject ,
                                content 
                            )
                 VALUES(?,?,?,?) '''
    # print(sql)
    # print(data)
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"../chapter6.db"

    conn = create_connection(database)
    with conn:
        for i in range(1, 300):
            article = (i, "홍길동", "Dummy subject: [%03d]" % i, "Dummy Content: [%03d]" % i)
            insert_dummy_data(conn,article)

if __name__ == '__main__':
    main()