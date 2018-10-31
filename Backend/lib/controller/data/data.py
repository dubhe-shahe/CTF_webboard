# -*- coding: utf-8 -*-
from lib.core.database.database import Mysql
from config.database import DBConfig
from lib.core.scripts.time import Time


class User:
    def __init__(self):
        user = DBConfig.user
        password = DBConfig.password
        host = DBConfig.host
        port = DBConfig.port
        db = DBConfig.db
        self.db = Mysql(user, password, host, port, db)
        # 加载数据库

    def checkuser(self, username):
        # check whether user exist return length of the output
        return len(self.db.select('Users', '', 'username=\''+username+'\''))

    def getinfo(self, uid):
        return self.db.select('Users', '', 'id=' + str(uid) + '')

    def getuserlist(self):
        print(self.db.select('Users'))
        return self.db.select('Users')

    def adduser(self, username, password, email, gender):
        # gender M男F女
        if self.checkuser(username) == 0:
            dt = Time.gettime()
            data = {
                'username': '\'' + username + ' \'',
                'password': '\'' + password + ' \'',
                'email': '\'' + email + ' \'',
                'gender': '\'' + gender + ' \'',
                'points': 0,
                'create_time': '\''+dt+'\'',
                'update_time': '\''+dt+'\''

            }
            return self.db.insert('Users', data)
        return False

    def changepass(self, uid, password):
        # change password
        dt = Time.gettime()
        data = {
            'password': '\'' + password + ' \'',
            'update_time': '\''+dt+'\''
        }
        return self.db.update('Users', data, 'id = {0}'.format(uid))

    def changeemail(self, uid, email):
        # change email
        dt = Time.gettime()
        data = {
            'email': '\'' + email + ' \'',
            'update_time': '\''+dt+'\''
        }
        return self.db.update('Users', data, 'id = {0}'.format(uid))

    def addpoints(self, uid, points):
        # add point to a user
        return self.db.add('Users', 'points', points, 'id = '+str(uid))

    def changesettings(self, uid, username, password, email, gender):
        # gender M男F女
        dt = Time.gettime()
        data = {
            'username': '\'' + username + ' \'',
            'password': '\'' + password + ' \'',
            'email': '\'' + email + ' \'',
            'gender': '\'' + gender + ' \'',
            'points': 0,
            'create_time': '\''+dt+'\'',
            'update_time': '\''+dt+'\''

        }
        return self.db.update('Users', data, 'id = {0}'.format(uid))


class Problem:
    def __init__(self):
        pass

    #检测题目是否存在
    def checkexit(self):
        pass

    #获取所有tag类的题目列表
    def getproblemlist(self):
        pass

    #获取所有tag类的题目列表
    def getproblemlist(self):
        pass

    #获取题目信息
    def getinfo(self):
        pass

    #添加题目
    def addproblem(self):
        pass

    #修改题目
    def editproblem(self):
        pass

    #删除题目
    def delproblem(self):
        pass

    #修改题目信息（管理员）
    def changesettings(self):
        pass

class WriteUp:
    def __init__(self):
        pass

    #检测WriteUp是否存在
    def checkexit(self):
        pass

    #获取writeup列表
    def getwriteuplist(self):
        pass

    #获取writeup信息
    def getinfo(self):
        pass

    #添加writeup
    def addwriteup(self):
        pass

    #删除writeup
    def delwriteup(self):
        pass

    #编辑writeup
    def editwriteup(self):
        pass

    #修改writeup信息(管理员)
    def changesettings(self):
        pass

class Record:
    def __init__(self):
        pass

    #获取Record列表
    def getrecordlist(self):
        pass

    #获取Record信息
    def getrecord(self):
        pass

    #添加Record
    def addrecord(self):
        pass

    #删除Record
    def delrecord(self):
        pass
