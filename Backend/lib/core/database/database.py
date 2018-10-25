#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql


class Mysql:
    """
        Mysql库用法：
            1.初始化数据库类
            2.start()
            3.执行操作
            4.stop()
        一定要stop!!
    """
    def __init__(self, user, password, host, port, db):
        self.__user = user
        self.__password = password
        self.__host = host
        self.__port = port
        self.__db = db
        self.__connected = False  # 判断是否start
        # 初始化各种变量

    def start(self):
        try:
            self.__conn = pymysql.connect(
                host=self.__host,
                user=self.__user,
                passwd=self.__password,
                port=self.__port,
                db=self.__db,
                charset='utf8mb4',  # 数据库编码类型
            )
            self.__cursor = self.__conn.cursor()
            self.__connected = True  # 成功就为True
            return True  # 调用时判断是否执行成功
        except pymysql.err as e:
            print("MySQL Error {0}:{1}".format(str(e.args[0]), str(e.args[1])))
            self.__connected = False
            return False

    def stop(self):
        if self.__connected:
            self.__cursor.close()
            self.__conn.close()
            self.__connected = False
            return True
        else:
            print("You have not connected to MySQL Database")
            return False

    def query(self, query):  # 执行query语句，返回所有结果
        if self.__connected:
            try:
                self.__cursor.execute(query)
                return self.__cursor.fetchall()
            except pymysql.err as e:
                print(
                    "MySQL Error " + str(e.args[0]) + ":" + str(e.args[1]))
                return False
        else:
            print("You have not connected to MySQL Database")
            return False

    def execute(self, query):  # 用于执行不需要返回值的语句，返回True 或 False
        if self.__connected:
            _bool = True  # 用于记录语句是否执行成功
            try:
                self.__cursor.execute(query)
                self.__conn.commit()
            except pymysql.err as e:
                print(
                    "MySQL Error " + str(e.args[0]) + ":" + str(e.args[1]))
                _bool = False
            finally:
                return _bool
        else:
            print("You have not connected to MySQL Database")
            return False

    def insert(self, table, data):
        # 数据库插入操作 这里如果有引号请自己在data中转义 无法自动判断
        if self.__connected:
            name = []
            value = []
            for key in data:
                name.append('`' + str(key) + '`')  # 这里的str是防止输入的是数字
                value.append(str(data[key]))
            query = 'insert into `' + table + \
                '` (' + ','.join(name) + ') values (' + ','.join(value) + ')'
            return self.execute(query)
        else:
            print("You have not connected to MySQL Database")

    def delete(self, table, where='1=2'):
        # 删除行 一定不要把where写成永远为真的值
        if self.__connected:
            query = 'delete from `' + table + '` where ' + where
            return self.execute(query)
        else:
            print("You have not connected to MySQL Database")

    def update(self, table, data, where='1=2'):
        # 更新行 记得如果是字符串单引号转义
        if self.__connected:
            sets = []
            for key in data:
                sets.append('`' + str(key) + '`=' + str(data[key]))
            query = 'update `' + table + '` set ' + ','.join(sets) + ' where ' + where
            return self.execute(query)
        else:
            print("You have not connected to MySQL Database")

    def select(self, table, key, where, suffix=''):
        # select行 suffix是指如果要查询order by ,union之类的东西写的
        if self.__connected:
            if len(key) == 0:
                key = ['*']
            value = ','.join(key)
            query = 'select ' + value + ' from `' + table + '` where ' + where + ' ' + suffix
            return self.query(query)
        else:
            print("You have not connected to MySQL Database")


if __name__ == "__main__":
    pass
