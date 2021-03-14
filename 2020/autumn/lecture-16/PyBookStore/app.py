# This is going to be a book store
# We would like to Create (Add), Checkout (Remove), Update and Read titles

# This app uses the rather simple Flask framework
from flask import Flask
from flask import request
import json
app = Flask(__name__)

# We are using a static book store. Nothing fancy
books = [
    {
        'isbn': '1473200261',
        'name': 'Witches abroad',
        'author': 'Terry Pratchett'
    },
    {
        'isbn': '006051518X',
        'name': 'Anansi boys',
        'author': 'Neil Gaiman'
    }
]

# Routes define your API endpoints, if you will
# @app.route() is called a Decorator - it "decorates" a function
# This route is a dynamic route that can contain the ISBN of a book
@app.route("/Books", methods=['GET'])
@app.route("/Books/<isbn>", methods=['GET'])
def get_books(isbn=None):
    books_to_return = books.copy()

    if isbn:
        books_to_return = [book for book in books if book['isbn'] == isbn]

    if 'author' in request.args:
        books_to_return = [
            book for book in books if book['author'] == request.args['author']]

    if len(books_to_return) == 0:
        response = app.response_class(
            status=404
        )
    else:
        response = app.response_class(
            response=json.dumps(books_to_return),
            status=200,
            mimetype='application/json'
        )

    return response

# The same route is now added with a POST method
# We want new books to be added and use the request body to send this data
# The entire request is stored in the request variable, and the body
# is contained in request.data
@app.route("/Books", methods=['POST'])
def add_books():
    try:
        request_data = request.json
        print('req ok')
        new_book = {
            'isbn': request_data['isbn'],
            'name': request_data['name'],
            'author': request_data['author']
        }
        
        if any(book.get('isbn', None) == new_book['isbn'] for book in books):
            return app.response_class(
                response= f'Uh oh... book with ISBN {new_book["isbn"]} already exists',
                status=409
            )

        books.append(new_book)
        return app.response_class(
            status=204
        )
    except:
        return app.response_class(
            response='Uh oh... This was not supposed to happen :(',
            status=404
        )

# This route is a dynamic route that can contain the ISBN of a book
@app.route("/Books/<isbn>", methods=['DELETE'])
def delete_book(isbn):
    filtered_books = [book for book in books if book['isbn'] != isbn]
    books.clear()
    for book in filtered_books:
        books.append(book)
    return app.response_class(
        status=204
    )
