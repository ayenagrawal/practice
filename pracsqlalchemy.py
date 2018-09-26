from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, request, redirect, Flask, flash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///D:\python\students.db'
# r"C:\Users\ayen.agrawal\Downloads\students.db
app.config['SECRET_KEY'] = r'l\xd4K\xf3h\xd1KT\xde\x9c\xc8\x17\xce\t&\xd4\xa9\xbf\xaf\xddd@\xbbD'
db = SQLAlchemy(app)

'''student table mapper class'''


class student(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    city = db.Column(db.String(20))
    addr = db.Column(db.String(50))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


@app.route('/')
def index():
    return '<h1 align=center style="color:maroon">Welcome to SQLAlchemy practice program</h1>' + render_template('home.html')


'''handler for adding a new record to student table in students database'''


@app.route('/addrow', methods=['GET', 'POST'])
def addrow():
    if request.method == 'POST':
        if request.form['name'] and request.form['city'] and request.form['addr'] and request.form['pin']:
            tbobj = student(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])
            db.session.add(tbobj)
            db.session.commit()
            flash('Data successfully inserted')
            return redirect(url_for('showrec'))
        else:
            flash('Please enter data in all fields')
    return render_template('addrec.html')


'''handler for displaying all records on the screen'''


@app.route('/showrec')
def showrec():
    return render_template('showrec.html', rows=student.query.all())


if __name__ == '__main__':
    app.run(debug=True)
