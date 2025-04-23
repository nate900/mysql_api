from flask import Flask, render_template, jsonify, request
from connection import get_connection

# get a connection from mysql database
conn = get_connection()
cursor = conn.cursor()


host = '127.0.0.1'
port = 8080

app = Flask(__name__)

# home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/icmp-types')
def icmp_types():
    return render_template('icmp-types.html')

@app.route('/planes')
def planes():
    return render_template('planes.html')

# small api to interact with my database
@app.route('/books', methods=['GET'])
def get_books():
    sql_statement = 'SELECT * FROM books;'
    cursor.execute(sql_statement)
    results = cursor.fetchall()
    return jsonify(results)



# Expecting
    # {
    #     book_name: name,
    #     year_of_book: year,
    #     book_desc: desc
    # }
@app.route('/books', methods=['POST'])
def insert_book():

    new_book = request.get_json()
    # Using parameterized queries to prevent SQL injection
    sql_statement = "INSERT INTO books (book_name, year_of_book, book_desc) VALUES (%s, %s, %s);"
    data = (new_book["book_name"], new_book["year_of_book"], new_book["book_desc"])

    cursor.execute(sql_statement, data)
    results = conn.commit()
    return jsonify(results)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    sql_statement = "DELETE FROM books WHERE id = (%s)"
    data = (id,)
    cursor.execute(sql_statement, data)
    results = conn.commit()
    return jsonify(results)

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)