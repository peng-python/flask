#encoding: utf-8
from flask import Flask,render_template,session,redirect,url_for
import flask
from exts import db
from forms import RegisteForm
from models import UserModel,ArticleModel
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


@app.route('/detail/<id>')
def detail(id):
    detail=ArticleModel.query.filter(ArticleModel.id==id).first()
    context={'detail':detail}
    return render_template('detail.html',**context)


@app.route('/delete/<id>')
def delete(id):
    article=ArticleModel.query.filter(ArticleModel.id==id).first()
    db.session.delete(article)
    db.session.commit()
    return redirect(url_for('design'))


@app.route('/design/')
def design():
    if session.get('user_id'):
        print session.get('user_id')
        all_article=ArticleModel.query.all()
        # user=session.get('user_id')
        # print user
        # print user.id
        user1=UserModel.query.filter(UserModel.id == session.get('user_id')).first()
        context={'all_article': all_article,'user':user1}
        return render_template('design.html', **context)
    else:
        return redirect(url_for('login'))


@app.route('/insert/',methods=['GET','POST'])
def insert():
    if flask.session.get('user_id'):
        if flask.request.method == 'GET':
            user1 = UserModel.query.filter(UserModel.id == session.get('user_id')).first()
            context={'user':user1}
            return flask.render_template('insert.html',**context)
        else:
            title=flask.request.form.get('title')
            article=flask.request.form.get('content')
            article_all=ArticleModel(title=title,article=article)
            db.session.add(article_all)
            db.session.commit()
            return u'发布成功！'
    else:
        return redirect(url_for('login'))
    # return render_template('insert.html')


@app.route('/')
def index():
    all_article=ArticleModel.query.order_by('-id').all() #将结果倒序排列
    context={'all_article':all_article}
    return render_template('index.html',**context)


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))



@app.route('/login/',methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return flask.render_template('login.html')
    else:
        username=flask.request.form.get('username')
        password=flask.request.form.get('password')
        user=UserModel.query.filter(UserModel.username==username,UserModel.password==password).first()
        # if user and user.check_password(password):
        #     flask.session['id']=user.id
        #     flask.g.user=user
        #     return flask.redirect(flask.url_for('index'))
        # print user
        if user:
            session['user_id']=user.id
            session.permanent=True
            return redirect(url_for('insert'))
        else:
            return u'用户名或密码错误！'
    # return render_template('login.html')


@app.route('/register/',methods=['GET', 'POST'])
def register():
    if flask.request.method == 'GET':
        return flask.render_template('register.html')
    else:
        form=RegisteForm(flask.request.form)
        if form.validate():
            username=form.username.data
            password=form.password.data
            user=UserModel(username=username,password=password)
            db.session.add(user)
            db.session.commit()
    return flask.redirect(flask.url_for('login'))
    # return render_template('register.html')


if __name__ == '__main__':
    app.run()
