from flask import Flask, request
from flask.views import MethodView

app = Flask(__name__)


class BaseApi(MethodView):
    # just a exampler script
    def get(self, abc):
        if abc:
            return "value of abc is: " + abc
        else:
            return "<h2>Inside MethodView Get method</h2>"

    def post(self):
        # jsondata = request.form.get('Name')
        jsondata = request.get_json()
        return "Captured data from POST method" + str(jsondata)


view = BaseApi.as_view('base')
app.add_url_rule("/", defaults={'abc': None}, view_func=view)
app.add_url_rule("/<string:abc>", view_func=view, methods=['GET'])


if __name__ == '__main__':
    app.run(debug=True)
