from flask import render_template, flash, url_for
from app import db
from app.main import bp
from app.models import User, Session, Event
from flask_login import current_user, login_required


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')

@bp.route('/sessions', methods = ['GET', 'POST'])
@login_required
def sessions():
    posts = current_user.get_location_sessions()
    return render_template('sessions.html', posts = posts)