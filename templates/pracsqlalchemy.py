from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, request, redirect, Flask, route

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'SQLITE:///students.sqlite3'
# r"C:\Users\ayen.agrawal\Downloads\students.db
app.config['SECRET_KEY'] = r'l\xd4K\xf3h\xd1KT\xde\x9c\xc8\x17\xce\t&\xd4\xa9\xbf\xaf\xddd@\xbbD'
db = SQLAlchemy(app)


class student(db.Model):
    id = db.Coloumn('student_id', db.Integer, primary_key=True)
    name = db.Coloumn(db.String(20))
    city = db.Coloumn(db.String(20))
    addr = db.Coloumn(db.String(50))
    pin = db.Coloumn(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/addrow')
def addrow():
    pass


@app.route('/showrec')
def showrec():
    return render_template('showrec.html', rows=student.query.all())


if __name__ == '__main__':
    app.run(debug=True)
