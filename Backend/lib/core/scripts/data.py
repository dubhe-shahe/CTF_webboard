# -*- coding: utf-8 -*-
import hashlib
import re
from config.security import *

def cleandata(l):
    r = {}
    i = 1;
    for role in l:
        k = {}
        for key in role:
            k.update({key: str(role[key])})
        r.update({str(i): k})
        i += 1
    print(r)
    return r


def filter(text):
    newtext = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+","",text)
    # 我觉得你这个地方可能会有些问题，应该是替换成转义字符，不是全去掉 Luty 你注意一下。
    return newtext


def encode(text):
    return hashlib.sha1(text+SecurityConfig.salt).hexdigest()


if __name__ == "__main__":
    pass
