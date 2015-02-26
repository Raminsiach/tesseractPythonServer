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
    return template('result', value=textify.toText(os.getcwd() + '/' + save_path + upload.filename))

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static/')
    

run(host='localhost', port=8080)