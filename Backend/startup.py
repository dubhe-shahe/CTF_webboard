from flask import Flask, request
from flask_restful import Resource, Api
from lib.method.Users import *

app = Flask(__name__)
api = Api(app)
# Users
api.add_resource(Users, '/user/<string:uid>')
api.add_resource(Users, '/user/')

if __name__ == '__main__':
    app.run(debug=True)