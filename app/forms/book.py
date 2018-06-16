"""
created by 朝文天下 on 

"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

__author__ = '朝文天下'


class SearchForm(Form):
    q = StringField(validators=[
        DataRequired(message='参数q,不能为空'),
        Length(min=1, max=30)
    ])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
