# -*- coding: utf-8 -*-
from lib.core.database.database import Mysql
from config.database import DBConfig
import datetime


class User:
    def __init__(self):
        user = DBConfig.user
        password = DBConfig.password
        host = DBConfig.host
        port = DBConfig.port
        db = DBConfig.db
        self.db = Mysql(user, password, host, port, db)
        # 加载数据库

    def adduser(self, username, password, email, gender):
        # gender M男F女
        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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

    def changesettings(self, uid, username, password, email, gender):
        # gender M男F女
        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
    
