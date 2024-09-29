from flask import Flask, render_template
from models import Book, db

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def main():
    book_list = Book.query.all()
    return render_template('books.html', books=book_list)

@app.route('/<title>')
def book_view(title):
    book = Book.query.filter_by(title=title).first()
    return render_template('book.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)