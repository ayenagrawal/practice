from formstruc import formStruct
from flask import Flask, request, flash, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = r'\x81\xf3.m\x12F/8\x9b\xb1U\x84\x9e\xbbb\xa9\xf9R\xe7Q\xa9k\xb1\xb1'


@app.route('/contact', methods=['GET', 'POST'])
def mainform():
    formobj = formStruct()
    if request.method == 'POST':
        if formobj.validate() == False:
            flash('All fields required.')
            return render_template('contact.html', form=formobj)
        else:
            return '<h2>Success inputting data</h2>'
    elif request.method == 'GET':
        return render_template('contact.html', form=formobj)


if __name__ == '__main__':
    app.run(debug=True)
