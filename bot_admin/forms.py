from flask_wtf import FlaskForm
import wtforms
from wtforms import validators


class LoginForm(FlaskForm):
    username = wtforms.StringField(
        label='Username',
        validators=[validators.DataRequired()],
        render_kw={"type": "username", 'placeholder': 'Username'}
    )
    password = wtforms.PasswordField(
        label='Password',
        validators=[validators.DataRequired()],
        render_kw={"type": "password", 'placeholder': 'Password'}
    )
    submit = wtforms.SubmitField(label='login')
