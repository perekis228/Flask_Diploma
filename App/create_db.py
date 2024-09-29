from flask import Flask
from models import Book, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # создаем тестовых исполнителей
        for i in range(10):
            book = Book(title=f'title{i}', author=f'author{i}', genre=f'genre{i}', description=f'desc{i}')
            db.session.add(book)
        db.session.commit()