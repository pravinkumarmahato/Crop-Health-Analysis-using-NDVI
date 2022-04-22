# -*- coding: utf-8 -*-
"""
    :author: Grey Li <withlihui@gmail.com>
    :copyright: (c) 2017 by Grey Li.
    :license: MIT, see LICENSE for more details.
"""
import os
import generate
from flask import Flask, render_template, request, redirect
from flask_dropzone import Dropzone

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.update(
    UPLOADED_PATH_nir=os.path.join(basedir, 'uploads/nir/'),
    UPLOADED_PATH_rgb=os.path.join(basedir, 'uploads/rgb/'),
    # Flask-Dropzone config:
    DROPZONE_MAX_FILE_SIZE=1024,  # set max size limit to a large number, here is 1024 MB
    DROPZONE_TIMEOUT=5 * 60 * 1000  # set upload timeout to a large number, here is 5 minutes
)

dropzone = Dropzone(app)

@app.route('/main', methods = ['GET'])
def main():
    return render_template('home.html')

@app.route('/rgbupload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH_rgb'], f.filename))
        # return redirect("/nir")
        # print("hogaya")
    return render_template('app.html')
    # return redirect("/nir")

@app.route('/nirupload', methods=['POST', 'GET'])    
def upload_nir():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH_nir'], f.filename))
        print("hogaya")
    return render_template('nirupload.html')
    # return "hey there"

@app.route('/get', methods=['GET'])
def getindex():
    # return "Calculating..."
    generate.get_index()
    return "Calculating..."


if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 1234, debug=True)
