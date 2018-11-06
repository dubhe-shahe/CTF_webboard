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
        return len(self.db.select('Users', '', 'username=\'' + username + '\''))

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
                'create_time': '\'' + dt + '\'',
                'update_time': '\'' + dt + '\''

            }
            return self.db.insert('Users', data)
        return False

    def changepass(self, uid, password):
        # change password
        dt = Time.gettime()
        data = {
            'password': '\'' + password + ' \'',
            'update_time': '\'' + dt + '\''
        }
        return self.db.update('Users', data, 'id = {0}'.format(uid))

    def changeemail(self, uid, email):
        # change email
        dt = Time.gettime()
        data = {
            'email': '\'' + email + ' \'',
            'update_time': '\'' + dt + '\''
        }
        return self.db.update('Users', data, 'id = {0}'.format(uid))

    def addpoints(self, uid, points):
        # add point to a user
        return self.db.add('Users', 'points', points, 'id = ' + str(uid))

    def changesettings(self, uid, username="", password="", email="", gender=""):
        # gender M男F女

        dt = Time.gettime()
        data = {
            'update_time': '\'' + dt + '\'',
        }
        if username != "":
            data["username"] = '\'' + username + ' \''
        if password != "":
            data["password"] = '\'' + password + ' \''
        if email != "":
            data["email"] = '\'' + email + ' \''
        if gender != "":
            data["gender"] = '\'' + gender + ' \''

        return self.db.update('Users', data, 'id = {0}'.format(uid))


class Problem:

    def __init__(self):
        user = DBConfig.user
        password = DBConfig.password
        host = DBConfig.host
        port = DBConfig.port
        db = DBConfig.db
        self.db = Mysql(user, password, host, port, db)

    def checkexit(self, name):
        return len(self.db.select('Problems', '', 'name=\'' + name + '\''))

    # 获取所有tag类的题目列表
    def getproblemlist(self):
        data = self.db.select('Problems')
        if len(data) == 0:
            return False
        else:
            return data

    # 获取所有tag类的题目列表
    def gettaglist(self, tag):
        data = self.db.select('Problems', '', 'tag=\'' + tag + '\'')
        if len(data) == 0:
            return False
        else:
            return data

    # 获取题目信息
    def getinfo(self, pid):
        return self.db.select('Problems', '', 'id=' + str(pid) + '')

    # 添加题目(管理员)
    def addproblem(self, name, tag, content, flag, points):
        dt = Time.gettime()
        data = {
            'name': '\'' + name + ' \'',
            'tag': '\'' + tag + '\'',
            'content': '\'' + content + '\'',
            'flag': '\'' + flag + '\'',
            'points': '\'' + points + '\'',
            'create_time': '\'' + dt + '\'',
            'update_time': '\'' + dt + '\''
        }
        try:
            result = self.db.insert('Problems', data)
        except Exception as e:
            print(e)
            return False
        return result

    # 修改题目(管理员)
    def editproblem(self, pid, name="", tag="", content="", flag="", points=""):
        data = {}
        dt = Time.gettime()
        data['update_time'] = '\'' + dt + '\''
        if name != "":
            data['name'] = '\'' + name + '\''
        if tag != "":
            data['tag'] = '\'' + tag + '\''
        if content != "":
            data['content'] = '\'' + content + '\''
        if flag != "":
            data['flag'] = '\'' + flag + '\''
        if points != "":
            data['points'] = '\'' + points + '\''

        return self.db.update('Problems', data, 'id = {0}'.format(pid))

    # 删除题目(管理员)
    def delproblem(self, name):
        if self.checkexit(name) != 0:
            self.db.delete('Problems', 'name=' + str(name) + '')

    # 修改题目信息（管理员）
    def changesettings(self):
        pass


class WriteUp:
    def __init__(self):
        user = DBConfig.user
        password = DBConfig.password
        host = DBConfig.host
        port = DBConfig.port
        db = DBConfig.db
        self.db = Mysql(user, password, host, port, db)

    # 检测WriteUp是否存在
    def checkexit(self, title):
        return len(self.db.select('WriteUp', '', 'title=\'' + title + '\''))

    # 获取writeup列表
    def getwriteuplist(self):
        print(self.db.select('WriteUp'))
        return self.db.select('WriteUp')

    # 获取writeup信息
    def getinfo(self, wid):
        return self.db.select('WriteUp', '', 'id=' + str(wid) + '')

    # 添加writeup
    def addwriteup(self, uid, pid, title, content):
        dt = Time.gettime()
        data = {
            'uid': '\'' + uid + ' \'',
            'pid': '\'' + pid + ' \'',
            'title': '\'' + title + ' \'',
            'content': '\'' + content + ' \'',
            'create_time': '\'' + dt + '\'',
            'update_time': '\'' + dt + '\''
        }
        try:
            result = self.db.insert('WriteUp', data)
        except Exception as e:
            print(e)
            return False
        return result

    # 删除writeup
    def delwriteup(self, title):
        if self.checkexit(title) != 0:
            return self.db.delete('WriteUp', 'title=' + str(title) + '')

    # 编辑writeup
    def editwriteup(self, title, content):
        dt = Time.gettime()
        if self.checkexit(title) != 0:
            data = {
                'title': '\'' + title + ' \'',
                'content': '\'' + content + ' \'',
                'update_time': '\'' + dt + '\''
            }
            try:
                result = self.db.update('WriteUp', data, 'title = {0}'.format(title))
            except Exception as e:
                print(e)
                return False
            return result

    # 修改writeup信息(管理员)
    def changesettings(self):
        pass


class Record:
    def __init__(self):
        user = DBConfig.user
        password = DBConfig.password
        host = DBConfig.host
        port = DBConfig.port
        db = DBConfig.db
        self.db = Mysql(user, password, host, port, db)

    def checkexit(self, rid):
        return len(self.db.select('Record', '', 'id=\'' + rid + '\''))

    # 获取Record列表
    def getrecordlist(self):
        print(self.db.select('Record'))
        return self.db.select('Record')

    # 获取Record信息
    def getrecord(self, rid):
        if self.checkexit(rid) != 0:
            try:
                result = self.db.select('Record', '', 'id=\'' + rid + '\'')
            except Exception as e:
                print(e)
                return False
            return result

    # 添加Record
    def addrecord(self, uid, pid, state):
        dt = Time.gettime()
        data = {
            'uid': '\'' + uid + ' \'',
            'pid': '\'' + pid + ' \'',
            'state': '\'' + state + ' \'',
            'create_time': '\'' + dt + '\'',
            'update_time': '\'' + dt + '\''
        }
        try:
            result = self.db.insert('Record', data)
        except Exception as e:
            print(e)
            return False
        return result

    # 删除Record
    def delrecord(self):
        pass
