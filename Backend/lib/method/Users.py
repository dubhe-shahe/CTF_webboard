# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import request
from lib.controller.data.data import User
from lib.core.scripts.data import *


class Users(Resource):
    User = User()

    def put(self):
        username = filter(request.form['username'])
        password = encode(request.form['password'])  #加盐加密 Sha1
        email = filter(request.form['email'])
        gender = filter(request.form['gender'])
        if self.User.adduser(username, password, email, gender):
            return {
                'ret': 200
            }
        else:
            return {
                'ret': 500
            }

    def get(self, uid):
        ret = cleandata(self.User.getinfo(filter(uid)))
        if ret:
            return ret
        else:
            return {'ret': 404}


class UserGetAll(Resource):
    User = User()

    def get(self):
        return cleandata(self.User.getuserlist())


class UserChangePass(Resource):
    User = User()

    def put(self, uid):
        former = request.form['former']
        later = request.form['later']
        ret = cleandata(self.User.getinfo(filter(uid)))
        if ret['password'] == encode(former):
            if self.User.changepass(filter(uid),encode(later)):
                return {
                    'ret': 200
                }
            else:
                return {
                    'ret': 500
                }
        return {
            'ret': 500
        }


class UserChangeEmail(Resource):
    User = User()

    def put(self, uid):
        former = request.form['former']
        later = request.form['later']
        ret = cleandata(self.User.getinfo(filter(uid)))
        if ret['password'] == filter(former):
            if self.User.changeemail(filter(uid),filter(later)):
                return {
                    'ret': 200
                }
            else:
                return {
                    'ret': 500
                }
        return {
            'ret': 500
        }


if __name__ == "__main__":
    pass
