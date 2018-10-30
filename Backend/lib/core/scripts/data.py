# -*- coding: utf-8 -*-
import hashlib
from config.security import *

def cleandata(dicts):
    r = {}
    for role in dicts:
        k = {}
        for key in role:
            k.update({key: str(dicts[key])})
        r.update(k)
    return r


def filter(text):
    return text


def encode(text):
    return hashlib.sha1(SecurityConfig.salt+text+SecurityConfig.salt).hexdigest()


if __name__ == "__main__":
    pass
