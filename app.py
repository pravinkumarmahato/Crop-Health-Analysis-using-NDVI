import os
import generate
from flask import Flask, render_template, request, redirect, flash, json
from flask_dropzone import Dropzone
from PIL import Image
import delete

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = "secret"

app.config.update(  
    UPLOADED_PATH_nir=os.path.join(basedir, 'uploads/nir/'),
    UPLOADED_PATH_rgb=os.path.join(basedir, 'uploads/rgb/'), 
    # Flask-Dropzone config:
    DROPZONE_MAX_FILES = 1,
    DROPZONE_MAX_FILE_SIZE=1024,  # set max size limit to a large number, here is 1024 MB
    DROPZONE_TIMEOUT=5 * 60 * 1000  # set upload timeout to a large number, here is 5 minutes
)

app.config["CACHE_TYPE"] = "null"

dropzone = Dropzone(app) 
# cache.init_app(app)
    
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/main', methods = ['GET'])
def main():
    return render_template('front.html')

@app.route('/test-static', methods = ['GET'])
def test_static():
    return '''<!DOCTYPE html>
<html>
<head>
    <title>Static File Test</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <style>
        body {
            background-image: url('/static/img/bg.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            height: 100vh;
        }
        .test-container {
            background: rgba(255,255,255,0.8);
            padding: 20px;
            margin: 50px auto;
            max-width: 500px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="test-container">
        <h1 class="text-primary">Static File Test</h1>
        <p>If you can see the background image and Bootstrap styling, static files are working.</p>
        <img src="/static/img/bg.jpg" alt="Background test" style="max-width: 200px; height: auto;">
    </div>
</body>
</html>'''

@app.route('/rgbupload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH_rgb'], f.filename))
    return render_template('rgbupload.html')
    

@app.route('/nirupload', methods=['POST', 'GET'])    
def upload_nir():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH_nir'], f.filename))
    return render_template('nirupload.html')

@app.route('/get', methods=['GET'])
def getindex():
    path, dirs, rgbfiles = next(os.walk("./uploads/rgb/"))
    rgblen = len(rgbfiles)
    path, dirs, nirfiles = next(os.walk("./uploads/nir/"))
    nirlen = len(nirfiles)    
    if rgblen != 1 and nirlen != 1:
        delete.del_files()
        return "<h1>Error Please give the correct input and try again.</h1>"
    elif rgblen != 1 or nirlen != 1:
        delete.del_files()
        return "<h1>Error Please give the correct input and try again.</h1>"
    nirdir = os.listdir("./uploads/nir/")
    nir = Image.open("./uploads/nir/{fname}".format(fname = nirdir[0]))
    data2 = nir.getdata()
    if str(type(data2[0])) != "<class 'int'>":
        nir.close()
        delete.del_files()
        return "<h1>Error Please give the correct input and try again.</h1>"
    rgbdir = os.listdir("./uploads/rgb/")
    rgb = Image.open("./uploads/rgb/{fname}".format(fname = rgbdir[0]))
    data = rgb.getdata()    
    if str(type(data[1])) != "<class 'tuple'>":
        rgb.close()
        delete.del_files()
        return "<h1>Error Please give the correct input and try again.</h1>"
    
    else:
        generate.get_index()
        data = generate.get_index()
        flash('successfully calculated...')
        delete.del_files()
        return render_template("output.html", data = data)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 1234, debug=True)
