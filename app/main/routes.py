from flask import render_template, flash, url_for
from app import db
from app.main import bp
from app.models import User, Post
from flask_login import current_user, login_required


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html')