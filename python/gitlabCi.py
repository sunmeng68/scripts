#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 17:41
# @Author  : opsonly
# @Site    :
# @File    : gitlabCi.py
# @Software: PyCharm


from flask import Flask,request,render_template,make_response,Response
import json,os,re,requests
import subprocess

app = Flask(__name__)
null = ""
cmd = "/var/www/html/ladmin-devel/"
@app.route('/test',methods=['POST'])
def hello():
    json_dict = json.loads(request.data)

    name = json_dict['event_name']
    ref = json_dict['ref'][11:]
    project = json_dict['project']['name']

    if name == 'push' and ref == 'master':
        os.chdir(cmd)
        s = subprocess.getoutput('sudo -u nginx composer install')
        return Response(s)
    else:
        return Response('none')


if __name__ == '__main__':
    app.run()