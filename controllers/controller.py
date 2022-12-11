from flask import render_template, request, redirect
from app import app
from models.books import *
from models.book import *

@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/books/<index>')
def get(index):
    x = int(index)
    return render_template('moreinfo.html',title='More Info', book=books[x])

@app.route('/books', methods=['POST'])
def add():
    name = request.form['name']
    author = request.form['author']
    genre = request.form['genre']
    check_out= True if 'check_out' in request.form else False
    new_book = Book(name=name, author=author, genre=genre, check_out=check_out)
    add_book(new_book)
    return redirect('/books')

@app.route('/books/delete/<index>', methods=['POST'])
def delete(index):
    x = int(index)
    remove_book(x)
    return redirect('/books')
