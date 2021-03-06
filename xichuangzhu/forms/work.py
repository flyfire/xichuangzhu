# coding: utf-8
from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from ..uploadsets import workimages


class WorkReviewForm(Form):
    """Form for add and edit work review"""
    title = TextField('标题', [DataRequired("标题不能为空")])
    content = TextAreaField('内容', [DataRequired("内容不能为空")])


class WorkReviewCommentForm(Form):
    """Form for add comment to work review"""
    content = TextAreaField('回复', [DataRequired("回复不能为空")])


class WorkImageForm(Form):
    """Form for add and edit work image"""
    image = FileField('作品', [FileRequired('作品图片不能为空'),
                             FileAllowed(workimages, '不支持的图片格式')])