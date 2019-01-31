from flask import render_template, flash, url_for, redirect
from app import db
from app.main import bp
from app.models import User, Session, Event
from flask_login import current_user, login_required
from app.main.forms import SessionForm, EventForm


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')

@bp.route('/sessions', methods = ['GET', 'POST'])
@login_required
def sessions():
    form = SessionForm()
    if form.validate_on_submit():
        session = Session(title = form.title.data, description = form.description.data, location = form.location.data, datetime = form.datetime.data, master = current_user)
        db.session.add(session)
        db.session.commit()
        flash('Session successfully posted!')
        return redirect(url_for('main.sessions'))
    posts = current_user.get_location_sessions()
    return render_template('sessions.html', posts = posts, form = form)

@bp.route('/events', methods = ['GET', 'POST'])
@login_required
def events():
    eform = EventForm()
    if eform.validate_on_submit():
        event = Event(title = eform.title.data, description = eform.description.data, location = eform.location.data, datetime = eform.datetime.data, master = current_user)
        db.session.add(event)
        db.session.commit()
        flash('Session successfully posted!')
        return redirect(url_for('main.events'))
    posts = current_user.get_location_events()
    return render_template('events.html', posts = posts, eform = eform)
