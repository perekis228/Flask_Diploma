from flask import Flask, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, LoginManager, UserMixin, current_user
from models import Book, User, db
from form import RegistrationForm, BookForm

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager()
login_manager.init_app(app)

db.init_app(app)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data, age=form.age.data)
        db.session.add(user)
        db.session.commit()
        flash("You have been registered!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('books'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
    return render_template('login.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/books/', methods=['GET', 'POST'])
def books():
    filter_by = request.args.get('filter')
    if filter_by == 'title':
        book_list = Book.query.order_by(Book.title.asc()).all()
    elif filter_by == 'author':
        book_list = Book.query.order_by(Book.author.asc()).all()
    elif filter_by == 'genre':
        book_list = Book.query.order_by(Book.genre.asc()).all()
    else:
        book_list = Book.query.all()

    form = BookForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            author = form.author.data
            genre = form.genre.data
            description = form.description.data
            new_book = Book(title=title, author=author, genre=genre, description=description)
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('books'))
    # book_list = Book.query.all()
    return render_template('books.html', books=book_list, admin=current_user.admin, form=form)

@app.route('/<title>')
def book_view(title):
    book = Book.query.filter_by(title=title).first()
    return render_template('book.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)