import sqlite3 as sql
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/addrow')
def addrow():
    return render_template('addrow.html')


@app.route('/addrec', methods=['GET', 'POST'])
def addrec():
    if request.method == 'POST':
        try:
            name = request.form['nm']
            id1 = request.form['id']
            address = request.form['addr']
            pincode = request.form['pin']
            with sql.connect(r"C:\Users\ayen.agrawal\Downloads\database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Students (Name,Id,Address,Pincode) VALUES (?,?,?,?)", (name, id1, address, pincode))
                con.commit()
                msg = "successfully added"
        except:
            con.rollback()
            msg = "Error while adding a row"
        finally:
            return render_template('result.html', msg=msg)
            con.close()


@app.route('/showrec')
def showrec():
    con = sql.connect(r"C:\Users\ayen.agrawal\Downloads\database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM Students")
    rows = cur.fetchall()
    return render_template('list.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
