from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired(),Length(max=32)])
    content = CKEditorField('Content')
    submit = SubmitField('Post')
