from bottle import route, run, template, request, static_file
from ctypes import *
import os
import textify


@route('/')
def index():
    return template('index')

@route('/upload', method = 'POST')
def doUpload():
    upload = request.files.get('upload')
    save_path = 'uploads/'
    upload.save(save_path)
    filePath = os.getcwd() + '/' + save_path + upload.filename
    value=textify.toText(filePath)
    os.remove(filePath)
    return template('result', value=value)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static/')
    

run(host='localhost', port=8080)