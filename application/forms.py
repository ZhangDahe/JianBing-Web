from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from application.models import User


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    email = StringField('邮箱地址', validators=[DataRequired(), Email()])
    password = PasswordField('输入密码', validators=[DataRequired()])
    password2 = PasswordField(
        '重复输入密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('该名称已存在')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('该邮件地址已存在')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('邮箱地址', validators=[DataRequired(), Email()])
    submit = SubmitField('重置密码')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('输入密码', validators=[DataRequired()])
    password2 = PasswordField(
        '重新输入密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('重置密码')


class EditProfileForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    about_me = TextAreaField('自我介绍', validators=[Length(min=0, max=140)])
    submit = SubmitField('更新')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('该名称已存在')


class EmptyForm(FlaskForm):
    submit = SubmitField('发表')


class PostForm(FlaskForm):
    post = TextAreaField('想说点啥', validators=[DataRequired()])
    submit = SubmitField('发表')