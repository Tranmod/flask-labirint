from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class GameForm(FlaskForm):

    direction = SelectField('Выберите направление', choices=[('north', 'Север'), ('sout', 'Юг'), ('west', 'Запад'),
                                                             ('east', 'Восток')])
    stages = IntegerField('Укажите количество шагов', validators=[DataRequired()], default=1)
    user_name = StringField('')
    submit = SubmitField('В Путь!')

class UserNameForm(FlaskForm):
	
    user_name = StringField('Укажите Ваше имя', validators=[DataRequired(), Length(min=2,)])
    submit = SubmitField('Я готов(а)!')