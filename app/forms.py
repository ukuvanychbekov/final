from flask_wtf import FlaskForm
import wtforms as wf
from wtforms import validators



class UserForm(FlaskForm):
    username = wf.StringField('Пользователь', validators=[wf.validators.DataRequired()])
    password = wf.PasswordField('Пароль', validators=[wf.validators.DataRequired(), validators.Length(min=8, max=64)])
    submit = wf.SubmitField('OK')

    # def validate(self):
    #     dict1 = {
    #         'letter': 0,
    #         'number': 0,
    #         'symbol': 0
    #     }
    #     if not super().validate():
    #         return False
    #     for i in self.password.data:
    #         if i.isalpha():
    #             dict1['letter'] += 1
    #         if i.isdigit():
    #             dict1['number'] += 1
    #         if i == '!' or i == '@' or i == '#' or i == '$' or i == '%':
    #             dict1['symbol'] += 1
    #         else:
    #             pass
    #     if dict1['symbol'] == 0:
    #         self.password.errors.append('Пароль должен содержать символы')
    #         return False
    #     if dict1['number'] == 0:
    #         self.password.errors.append('Пароль должен содержать цифры')
    #         return False
    #     if dict1['letter'] == 0:
    #         self.password.errors.append('Пароль должен содержать буквы')
    #         return False
    #     return True

    def validate_password(self, field):
        dict1 = {
            'letter': 0,
            'number': 0,
            'symbol': 0
        }
        for i in field.data:
            if i.isalpha():
                dict1['letter'] += 1
            if i.isdigit():
                dict1['number'] += 1
            if i == '!' or i == '@' or i == '#' or i == '$' or i == '%':
                dict1['symbol'] += 1
            else:
                pass
        if dict1['symbol'] == 0:
            raise validators.ValidationError('Пароль должен содержать символы')
        if dict1['number'] == 0:
            raise validators.ValidationError('Пароль должен содержать цифры')
        if dict1['letter'] == 0:
            raise validators.ValidationError('Пароль должен содержать буквы')



class PostForm(FlaskForm):
    title = wf.StringField('Заголовок', validators=[wf.validators.DataRequired()])
    content = wf.TextAreaField('Текст новости', validators=[wf.validators.DataRequired()])
    is_boom_news = wf.BooleanField('Супер любовь')
    submit = wf.SubmitField('OK')