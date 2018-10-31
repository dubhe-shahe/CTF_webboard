#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

class Mysql:
    """
        Mysql库用法x
            1.初始化数据库类
            2.执行操作
    """
    def __init__(self, user, password, host, port, db):
        self.__user = user
        self.__password = password
        self.__host = host
        self.__port = port
        self.__db = db
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
            self.__cursor = self.__conn.cursor(pymysql.cursors.DictCursor)
            return True  # 调用时判断是否执行成功
        except Exception as e:
            print(e)
            return False

    def stop(self):
        try:
            self.__cursor.close()
            self.__conn.close()
        except Exception as e:
            print(e)

    def query(self, query):  # 执行query语句，返回所有结果
            try:
                self.start()
                self.__cursor.execute(query)
                self.__conn.commit()
                self.stop()
                return self.__cursor.fetchall()
            except Exception as e:
                self.__conn.rollback()
                print(e)
                return False
            finally:
                pass

    def execute(self, query):  # 用于执行不需要返回值的语句，返回True 或 False
        _bool = True  # 用于记录语句是否执行成功
        try:
            self.start()
            self.__cursor.execute(query)
            self.__conn.commit()
            self.stop()
        except Exception as e:
            _bool = False
            print(e)
            self.__conn.rollback()
            return False
        finally:
            return _bool

    def insert(self, table, data):
        # 数据库插入操作 这里如果有引号请自己在data中转义 无法自动判断
        name = []
        value = []
        for key in data:
            name.append('`' + str(key) + '`')  # 这里的str是防止输入的是数字
            value.append(str(data[key]))
        query = 'insert into `' + table + \
            '` (' + ','.join(name) + ') values (' + ','.join(value) + ')'
        return self.execute(query)

    def delete(self, table, where='1=2'):
        # 删除行 一定不要把where写成永远为真的值
        query = 'delete from `' + table + '` where ' + where
        return self.execute(query)

    def update(self, table, data, where='1=2'):
        # 更新行 记得如果是字符串单引号转义
        sets = []
        for key in data:
            sets.append('`' + str(key) + '`=' + str(data[key]))
        query = 'update `' + table + '` set ' + ','.join(sets) + ' where ' + where
        return self.execute(query)

    def select(self, table, key='', where='1=1', suffix=''):
        # select行 suffix是指如果要查询order by ,union之类的东西写的
        if len(key) == 0:
            key = ['*']
        value = ','.join(key)
        query = 'select ' + value + ' from `' + table + '` where ' + where + ' ' + suffix
        return self.query(query)

    def add(self, table, key, num, where='1=2'):
        query = 'update`' + table + '` set ' + key + ' = ' + key + '+' + str(num) + ' where' + where
        return self.execute(query)

