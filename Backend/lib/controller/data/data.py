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
        return self.db.update('Users', data, 'user = {0}'.format(uid))

    def changeemail(self, uid, email):
        # change email
        dt = Time.gettime()
        data = {
            'email': '\'' + email + ' \'',
            'update_time': '\''+dt+'\''
        }
        return self.db.update('Users', data, 'user = {0}'.format(uid))

    def addpoints(self, uid, points):
        # add point to a user
        return self.db.add('Users', 'points', points, 'uid = '+str(uid))

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
        return self.db.update('Users', data, 'user = {0}'.format(uid))