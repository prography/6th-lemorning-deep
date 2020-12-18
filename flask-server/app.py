from flask import Flask, redirect, render_template, request, url_for, flash
import os
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import time

app = Flask(__name__)

UPLOAD_FOLDER = './uploads/audio'
ALLOWED_EXTENSIONS = set(['m4a', 'm4p', 'wav', 'mp3', 'mp4'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    return '''
    <h1>Deep Learning rending page</h1>
        <p>음악파일을 업로드 하면 딥러닝모델(musicnn)을 이용하여 어떤 종류의 음악인지 분류해 줍니다.</p>
        <a href='/tag'>Click Here!!!</a>
    '''


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



@app.route('/tag', methods=['GET', 'POST'])
def tag():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            #딥러닝 로직
            from deep.model import DeepModel
            model = DeepModel()
            path = UPLOAD_FOLDER +'/' +filename
            feats, tags = model.extract_info(path, mode='both', topN=5)
            return render_template('deeplearning.html', filename=filename, tags=tags)
        else:
            return '<h1>Error</h1>'

    return render_template('tag.html')



@app.route('/tag-optional', methods=['GET', 'POST'])
def tag_optional():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            #파일 변환
            from deep.audio_transfer import getstatusoutput
            path = UPLOAD_FOLDER +'/' +filename
            outputdir = os.path.join(UPLOAD_FOLDER, 'm4a')
            for root, dirs, files in os.walk(outputdir):
                for f in files:
                    path = os.path.join(root, f)
                    base, ext = os.path.splitext(f)
                    outputpath = os.path.join(outputdir, base + ".wav")
                    if ext == '.m4a':
                        status, output = getstatusoutput('ffmpeg -i "%s" "%s"' % (path, outputpath))

                        #딥러닝 로직
            from deep.model import DeepModel
            time.sleep(30)
            model = DeepModel()
            feats, tags = model.extract_info(output, mode='both', topN=5)

            return render_template('deeplearning.html', filename=filename, tags=tags)

        else:
            return '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>File Select Error!</h1>
            '''

    return '''
    <!doctype html>
    <title>Upload music File</title>
    <h1>Upload music File(m4a)</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    <p>파일변환에 시간이 소요됩니다. 약 1분정도 기다려 주세요 :D</p>
    '''


if __name__ == '__main__':
    app.run(debug=True)