#encoding: utf-8
from exts import db


class UserModel(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(100),nullable=False)
    password=db.Column(db.String(100),nullable=False)


class ArticleModel(db.Model):
    __tablename__="article"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(100),nullable=False)
    article=db.Column(db.Text,nullable=False)
    author_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    author=db.relationship('UserModel',backref=db.backref('articles'))