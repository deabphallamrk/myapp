from wtforms import Form, StringField, TextAreaField, SubmitField, ValidationError
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

class FRM_PAGE(FlaskForm):
    title       = StringField("Title", validators=[DataRequired()])
    content     = TextAreaField("Content", validators=[DataRequired()])
    submit      = SubmitField("Submit")



    
