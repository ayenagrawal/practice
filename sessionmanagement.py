from flask import Flask, url_for, redirect, session, request, abort, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = r'\x81\xf3.m\x12F/8\x9b\xb1U\x84\x9e\xbbb\xa9\xf9R\xe7Q\xa9k\xb1\xb1'
# session management


@app.route('/add')
def func1():
    if 'count1' in session:
        session['count1'] = session.get('count1') + 1
    else:
        session['count1'] = 1
    return 'Total Visits: %d' % session.get('count1')


@app.route('/del')
def func2():
    session.pop('count1', None)
    return 'Visitors count reset...'


@app.route('/')
def index():
    if 'username' in session:
        nm = session.get('username')
        return '<b>Welcome user : ' + nm + '<br/><a href="/logout">Click here to logout session</a></b>'
    else:
        return render_template('pq.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    else:
        if request.method == 'POST':
            if request.form['name'] == 'admin':
                session['username'] = request.form['name']
                return redirect(url_for('index'))
            else:
                return "Invalid Username!!!", 401
        return '''
            <form action="" method="post">
                Username:<br/>
                <input type=text name="name" placeholder=" Enter username *"><br/>
                <input type=submit value=submit>
            </form>
            '''


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
        msg = "Logged out session Successfully"
        return render_template('pq.html', msg=msg)
    else:
        msg = "No Active sessions found!!!"
        return render_template('pq.html', msg=msg)


if __name__ == '__main__':
    app.run(debug=True)
