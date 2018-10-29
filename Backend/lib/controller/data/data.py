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

    def checkuser(self,username):
        return len(self.db.select('Users', '', 'username=\''+username+'\''))

    def adduser(self, username, password, email, gender):
        # gender M男F女
        if self.checkuser(username)>0:
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
        dt = Time.gettime()
        data = {
            'password': '\'' + password + ' \'',
            'update_time': '\''+dt+'\''
        }
        return self.db.update('Users', data, 'user = {0}'.format(uid))

    def changeemail(self, uid, email):
        dt = Time.gettime()
        data = {
            'email': '\'' + email + ' \'',
            'update_time': '\''+dt+'\''
        }
        return self.db.update('Users', data, 'user = {0}'.format(uid))

    # def addpoints(self, uid, points):
    #     dt = Time.gettime()
    #     data = {
    #         'points': 0,
    #         'update_time': '\''+dt+'\''
    #     }
    #     return self.db.update('Users', data, 'user = {0}'.format(uid))
    # 这里可能是个坑

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
