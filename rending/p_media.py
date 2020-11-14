# from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import FileField
# from flask_uploads import configure_uploads, IMAGES, UploadSet
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'dkfhkjasehrkfgyklawnedkic2379'
# app.config['UPLOADED_IMAGES_DEST'] = '/Users/jooyoungson/6th-lemorning-deep/rending/music'
#
# musics = UploadSet('musics', IMAGES)
# configure_uploads(app, musics)
#
# class MyForm(FlaskForm):
#     music = FileField("music")
#
#
# @app.route("/", methods=["GET", "POST"])
# def index():
#     form = MyForm()
#     if form.validate_on_submit():
#         filename = musics.save(form.audio.data)
#         return f'Filename: { filename }'
#     return render_template("p_media.html")


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

if __name__ == '__main__':
    app.run(debug=True)
