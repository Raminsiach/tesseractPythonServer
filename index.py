from bottle import route, run, template, request
from ctypes import *
import os
import textify


@route('/')
def index():
    return '''
        <form action="/upload" method="POST" enctype="multipart/form-data">
        Select a file: <input type="file" name="upload" />
        <input type="submit" value="Start upload" />
        </form>
    '''

@route('/upload', method = 'POST')
def doUpload():
    upload = request.files.get('upload')
    save_path = 'uploads/'
    upload.save(save_path)
    return textify.toText(os.getcwd() + '/' + save_path + upload.filename);
    

run(host='localhost', port=8080)