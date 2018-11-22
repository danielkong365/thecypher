from flask import render_template, flash, url_for
from app import db
from app.main import bp
from app.models import User, Post


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    users = [{'username':'DK'}]
    posts = [{'master': {'username':'DK'}, 'location': 'ATL'}]
    return render_template('index.html', users=users, posts=posts)