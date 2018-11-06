# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import request
from lib.controller.data.data import Problem
from lib.core.scripts.data import *


class Problems(Resource):
    Problem = Problem()

    def put(self):
        name = filter(request.form['name'])
        tag = filter(request.form['tag'])
        content = filter(request.form['content'])
        flag = filter(request.form['flag'])
        points = filter(request.form['points'])
        if self.User.addproblem(name, tag, content, flag, points):
            return {
                'ret': 200
            }
        else:
            return {
                'ret': 500
            }

    def get(self, pid):
        ret = cleandata(self.Problem.getinfo(filter(pid)))
        if ret:
            return ret
        else:
            return {'ret': 404}


class ProblemGetAll(Resource):
    Problem = Problem()

    def get(self):
        return cleandata(self.Problem.getproblemlist())

class ProblemGetTagList(Resource):
    Problem = Problem()

    def get(self, tag):
        ret = cleandata(self.Problem.gettaglist(filter(tag)))
        if ret:
            return ret
        else: 
            return {'ret': 404}

if __name__ == "__main__":
    pass
