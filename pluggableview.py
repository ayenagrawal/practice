from flask import Flask
# from flask import request
from flask.views import View

app = Flask(__name__)

"""
@app.route("/", methods=['GET'])
def home():
    if request.method == "GET":
        return "<h2>This is homepage.</h2>"
"""


class ViewDemo(View):

    def dispatch_request(self):
        return "<h1>Using pluggable views!!!</h1>"


app.add_url_rule("/", view_func=ViewDemo.as_view('firstpage'))


if __name__ == '__main__':
    app.run(debug=True)
