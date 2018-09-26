from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


'''Flask first example'''

# using html content in python


@app.route('/')
def startpg():
    return '<font color = blue align = center><h1>This is the first page in flask setup</h1></font>'


@app.route('/user/<nm>')
def hello(nm):
    return 'Hello ' + nm

# url variable rule


@app.route('/blog/<int:postID>')
def blogger(postID):
    return 'This is blog ID ' + str(postID)


# binding a static page/js page
@app.route('/index')
def indexpage():
    return render_template('index.html')

# error handling and customised template


@app.errorhandler(404)
def handlerevnt(error):
    return render_template('abc.html'), 404

# user welcome screen after login


@app.route('/checked/<user>')
def func1(user):
    return '<h2>Welcome ' + user + '</h2>'

# fetching data from html form and checking method used for http


@app.route('/login', methods=['POST', 'GET'])
def checklogin():
    if request.method == 'POST':
        usernm = request.form['nm']
        return redirect(url_for('func1', user=usernm))
    elif request.method == 'GET':
        usernm = request.args.get('nm')
        return redirect(url_for('func1', user=usernm))
    else:
        return 'error'

# template adding


@app.route('/index/<name>')
def func2(name):
    return render_template('blank.html', name=name, pos='manager')


if __name__ == '__main__':
    app.run(debug=True)
