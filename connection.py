import mysql.connector

class ConnectionException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

def get_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mypassword',
        database='josiah_db'
    )

    if conn.is_connected():
        print('Connection was successful')
        return conn
    raise ConnectionException('Something went wrong with connecting to the mysql server.')
    