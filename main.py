from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Book.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable = False)
    author = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Book {self.id}'


@app.route('/')
def book():
    db.create_all()
    books = Book.query.all()
    return render_template("index.html", Book=books)


@app.route('/add_book', methods=['GET', 'POST'])
def submit_book():
    if request.method == "POST":
        author = request.form['author']
        title = request.form['title']
        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('book'))
    return render_template("submit.html")


if __name__ == '__main__':
    app.run(debug=True)
