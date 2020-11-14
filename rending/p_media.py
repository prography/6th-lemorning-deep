# image 파일 예제
# https://github.com/PrettyPrinted/youtube_video_code/tree/master/2020/01/06/Using%20Flask-WTF%20With%20Flask-Uploads

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_IMAGES_DEST'] = 'uploads/images'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

class MyForm(FlaskForm):
    image = FileField('image')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()

    if form.validate_on_submit():
        filename = images.save(form.image.data)
        return f'Filename: {filename}'

    return render_template('p_media.html', form=form)

####################################################
from flask_uploads import AUDIO

app.config['UPLOADED_AUDIOS_DEST'] = 'uploads/audios'
audios = UploadSet('audios', AUDIO)
configure_uploads(app, audios)

class AudioForm(FlaskForm):
    audio = FileField('audio')

@app.route('/audio', methods=['GET','POST'])
def audio():
    form = AudioForm()

    if form.validate_on_submit():
        audios.save(form.audio.raw_data)
#        filename = audios.save(form.audio.data)
        return 'uploaded?'

    return render_template('submit.html')

###########################################
#audio file 업로드 성공!
from flask import request
import os

UPLOAD_FOLDER = './uploads/audio'
ALLOWED_EXTENSIONS = set(['m4a', 'm4p', 'wav', 'mp3', 'mp4'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/hello")
def hello(name=None):
    return "please go to /file"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/uploaded_file")
def uploaded_file():
    return "<h1>OK!</h1>"


@app.route('/file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            #            filename = secure_filename(file.filename)
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "<h1>Ok!! </h1>"
        else:
            return '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>File Select Error!</h1>
            <a href="/file">file</a>
            '''

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
