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
        return {
            'ret': self.User.adduser(username, password, email, gender)
        }

    def get(self, uid):
        if uid == '':
            return cleandata(self.User.getuserlist())
        return cleandata(self.User.getinfo(filter(uid)))  # [0]获取第一号元素


class UserChangePass(Resource):
    User = User()

    def put(self,uid):
        former = request.form['former']
        later = request.form['later']
        ret = cleandata(self.User.getinfo(filter(uid)))
        if ret['password'] == encode(former):
            return self.User.changepass(filter(uid),encode(later))
        return False


class UserChangeEmail(Resource):
    User = User()

    def put(self,uid):
        former = request.form['former']
        later = request.form['later']
        ret = cleandata(self.User.getinfo(filter(uid)))
        if ret['password'] == filter(former):
            return self.User.changeemail(filter(uid),filter(later))
        return False


if __name__ == "__main__":
    pass
