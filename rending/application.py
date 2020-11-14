from flask import Flask, redirect, render_template, request, url_for, flash

import os
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

musics = []
UPLOAD_FOLDER = './music'
ALLOWED_EXTENSIONS = {'m4a', 'mp3', 'wav', 'm4p'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route("/")
def index():
    return "<h1>API rending page HTML ver</h1>"


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        music = request.form.get("FileName")
        musics.append(music)
        return redirect("/tag")
    else:
        return render_template("submit.html")


@app.route("/tag")
def tag():
    return "tag"


@app.route("/recommend")
def recommend():
    return "recommend"

if __name__ == '__main__':
    app.run(debug=True)
