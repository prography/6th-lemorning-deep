# 레모닝 딥러닝 API 

## block diagram

<img src='https://github.com/YunaSon/Prography/blob/master/P6-5_LEMORNING/img/%EC%A0%84%EC%B2%B4block.png'>

<img src='https://github.com/YunaSon/Prography/blob/master/P6-5_LEMORNING/img/flask%EB%82%B4%EB%B6%80block.png'>



## code
app.py
```

from flask import Flask, redirect, render_template, request, url_for, flash
import os

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
```


## Result

1. 음악 파일을 upload한다. 
<img src='https://github.com/YunaSon/Prography/blob/master/P6-5_LEMORNING/img/r1.png'>

2. 관련 Tag를 반환한다. 
<img src='https://github.com/YunaSon/Prography/blob/master/P6-5_LEMORNING/img/r2.png'>
