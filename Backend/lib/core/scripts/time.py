# -*- coding: utf-8 -*-
import datetime


class Time:

    @staticmethod
    def gettime():
        """
        数据库 datatime 返回模式
        """
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    pass