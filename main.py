from flask import Flask,  render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from utils import extract_top_hex_colours_from_image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'topsec'
Bootstrap(app)


class UploadForm(FlaskForm):
    file = FileField('Upload an Image File')
    submit = SubmitField('Submit')    


@app.route("/", methods=['GET', 'POST']) 
def index():
    image_name = 'default_image.jpeg'
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        image_name = secure_filename(file.filename)
        file.save(f"static/{image_name}")
    
    file_name = f"static/{image_name}" 
    hex_codes = extract_top_hex_colours_from_image(file_name)
    return render_template("index.html", form=form, image=image_name, hex_codes = hex_codes) 
 
if __name__ == '__main__':
    app.run(debug=True)
