from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)


class Login(Resource):
    def get(self):
        var1 = request.args.get('abc', type=int)
        if var1:
            return 'Square of {} is {}'.format(var1, var1**2)
        return 'You are inside Login get route'

    def post(self):
        var1 = request.get(var)
        return 'Square of {} is {}'.format(var1, var1**2)


api.add_resource(Login, '/')

if __name__ == '__main__':
    app.run(debug=True)
