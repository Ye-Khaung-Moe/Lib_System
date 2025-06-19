from flask import Flask,request, jsonify
from add import add_book

app = Flask(__name__)

@app.route('/add_book', methods=['POST'])
def add_book_route():
    data = request.json
    title = data.get('title')
    author = data.get('author')
    year = data.get('year')

    if not title or not author or not year:
        return jsonify({'error': 'Mission Data'}),400
    
    result = add_book(title,author,year)
    return jsonify({'message': result})





 
