from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #here we define the app
app.config['SQL_ALCHEMY_DATABASE_URI'] = 'sqlite:///Book.sqlite3'
db = SQLALchemy(app) #We set a database object


class Book(db.Model):
    """""
    Here I defined a model where I store objects to represent: Book is the model and id, title, author are rows
    """
    id = db.column("id", db.integer, primarykey=True)
    title = db.column(db.String(50))
    author = db.column(db.String(50))
    def __int__(self, title, author):
        self.title = title
        self.author = author

def addcontext():
    with app.app_context():
    db.create_all()



@app.route('/book') #I created a path here that can be accessed by /book. This shows the list of items stored in the database for Book. I used the model html file as exact as it was shown in lectures
def book():
    render_template("index.html", Book=Book.query.all())


@app.route('/add_book', methods=["GET","POST"])
def submit_book():
    return render_template("submit.html")


if __name__ == '__main__':
    create_db()
    app.run(port=5001, debug=True)
