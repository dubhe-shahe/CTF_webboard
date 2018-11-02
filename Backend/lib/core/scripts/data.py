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
    return newtext


def encode(text):
    return hashlib.sha1(text+SecurityConfig.salt).hexdigest()


if __name__ == "__main__":
    pass
