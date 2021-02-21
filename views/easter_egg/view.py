#this is where all the routes will go

from views.easter_egg import easter_egg_bp
from flask import Flask, render_template,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, FloatField,PasswordField
from wtforms.validators import InputRequired, Length, NumberRange
from views.easter_egg import model
from views.easter_egg import food
from flask_login import UserMixin, LoginManager
from flask_login import UserMixin, LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from views.easter_egg import db, User

app = Flask(__name__)
Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



class LoginForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(), Length(min=1,max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=1,max=80)])

class RegisterForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(), Length(min=1,max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=1,max=80)])
    grade = FloatField('grade',validators=[InputRequired()])
    id = FloatField('id',validators=[InputRequired()])

@easter_egg_bp.route('/') #this is the home page of the makeup API page
def index():
    return render_template("easter_egg/home.html")

@easter_egg_bp.route('/theeastercontacts')
def eastercontactus():
    return render_template("easter_egg/newcontactus.html", images=model.infoforthecontactsineaster())

@easter_egg_bp.route('/image_map_dnhs')
def image_map():
    return render_template("easter_egg/image_map_dnhs.html", images=model.infoforthecontactsineaster())

@easter_egg_bp.route('/Signup/',methods = ['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(name = form.username.data, Stu_id = form.id.data, password = form.password.data,grade = form.grade.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('easter_egg_bp.login'))

    return render_template("easter_egg/SU.html",form = form)

@easter_egg_bp.route('/Login', methods = ['GET', 'POST'])
def login():
    logform = LoginForm()

    if logform.validate_on_submit():
        #exists = db.session.query(
        #db.session.query(User).filter_by(username='AndrewZhang').exists()
        #).scalar()
        #if exists == True:
        #return "Exists"
        user = User.query.filter_by(username = logform.username.data).first()
        if user:
            if user.password == logform.password.data:
                return redirect(url_for('private'))

        return '<h1>Invalid username or password</h1>'

    return render_template("easter_egg/login.html",form = logform)


@easter_egg_bp.route('/auth_user', methods = ['GET','POST']) #this is the home page of the makeup API page
def private():
    return render_template("easter_egg/auth_user.html")

@login_required
@easter_egg_bp.route('/ordernow')
def timetoorder():
    return render_template("easter_egg/ordernow.html")

@easter_egg_bp.route('/multipage_form')
def multipage_from():
    return render_template("easter_egg/multipage_form.html", snack_list=food.inventory_stack())

@easter_egg_bp.route('/singlepage_form')
def singlepage_form():
    return render_template("easter_egg/singlepage_form.html", snack_list=food.inventory_stack())

