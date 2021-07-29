from . import main
from flask import render_template, request, redirect, url_for, flash, make_response, session, current_app
from flask_login import login_required, login_user,current_user, logout_user
from .. import db
from..models import Post
# from .models import User, Post, Category, Feedback, db
# from .forms import ContactForm, LoginForm
# from .utils import send_mail

from models import Post



@main.route('/', methods=['GET', 'POST'])
def index():
    posts = Post.query.all()
    return render_template('index.html' ,post=posts)



@main.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    return render_template('index.html', post= post)



@main.route('/loging/', methods=['GET', 'POST'])
def loging():
    return render_template('loging.html')


@main.route('/help')
def helper():
    return 'this is help page'


@main.route('/user/<int:id>/')
def user_profile(id):
    return "Profile page of user #{}".format(id)


@main.errorhandler(404)
def page_not_found(error):
    return render_template('page_404.html', title="Page not found")