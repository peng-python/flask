import wtforms
from wtforms import validators


class RegisteForm(wtforms.Form):
    username=wtforms.StringField(validators.length(min=6,max=20))
    password=wtforms.StringField(validators.length(min=5,max=20))
